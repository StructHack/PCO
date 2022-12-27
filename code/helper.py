from itertools import islice
from openpyxl import load_workbook

CTR = {
     'R1': 150/5,
    'R2': 100/5,
    'R3': 50/5,
    'R4': 50/5,
    'R5': 100/5,
    'R6': 100/5,
    'R7': 200/5,
    'R8': 200/5,
    'R9': 200/5,
    'R10': 100/5,
    'R11': 200/5,
    'R12': 100/5,
    'R13': 50/5,
    'R14': 50/5,
}

IP = {
    'R1': 1.2,
    'R2': 1.2,
    'R3': 1.2,
    'R4': 1.2,
    'R5': 1.2,
    'R6': 1.2,
    'R7': 1.2,
    'R8': 1.2,
    'R9': 1.2,
    'R10': 1.2,
    'R11': 1.2,
    'R12': 1.2,
    'R13': 1.2,
    'R14': 1.2,
}

CTR_eqn = {
     'R1': 'x(1)',
    'R2': 'x(2)',  
    'R3': 'x(3)',  
    'R4': 'x(4)',
    'R5': 'x(5)',
    'R6': 'x(6)',
    'R7': 'x(7)',
    'R8': 'x(8)',
    'R9': 'x(9)',
    'R10': 'x(10)',
    'R11': 'x(11)',
    'R12': 'x(12)',
    'R13': 'x(13)',
    'R14': 'x(14)',
}

#==== creating objective and constraints ====

def create_equation():
    total_eqn = ''
    constraints = []
    additional_constraints = []
    total_trip = {
        'R1': 0,
        'R2': 0,  
        'R3': 0,  
        'R4': 0,
        'R5': 0,
        'R6': 0,
        'R7': 0,
        'R8': 0,
        'R9': 0,
        'R10': 0,
        'R11': 0,
        'R12': 0,
        'R13': 0,
        'R14': 0
    }
    book = load_workbook('BUS DATA.xlsx')
    sheet = book['line_7']
    json_data = create_dict(sheet)
    
    #'R1': {'current': 2.431, 'backup': {'number': 1, 'name': ['R12'], 'backup_current': [0.199]}}
    
    for x in json_data:
        primary_relay_name = x # R1
        primary_current = json_data[x]['current'] # current: 2431
        if primary_current != None:
            primary_trip = tripping_time(primary_current, CTR[primary_relay_name], IP[primary_relay_name]) # calculation of tripping time
            # total_trip[primary_relay_name] = primary_trip
            total_trip[primary_relay_name] += primary_trip # for objective function adding all the same relay values
            
            additional_constraints.append('{}*{}'.format(primary_trip, CTR_eqn[primary_relay_name]))
            
            backup_number = json_data[x]['backup']['number'] # 'number' :1
            for bk in range(backup_number):
                back_name = json_data[x]['backup']['name'][bk] #'name':['R12'] 
                back_current = json_data[x]['backup']['backup_current'][bk] #backup_current: [0.199]
                back_trip = tripping_time(back_current, CTR[back_name], IP[back_name]) # calculation of tripping time
                
                if(back_trip > 0):
                    additional_constraints.append('{}*{} '.format(back_trip, CTR_eqn[back_name]))
                    total_trip[back_name] += back_trip # for objective function adding all the same relay values
                    constraints.append ('-{}*{}+{}*{} '.format(back_trip, CTR_eqn[back_name],primary_trip,CTR_eqn[primary_relay_name]))
        else:
            continue

    return [total_trip,constraints, additional_constraints]

# ==== formatting equation ===

def format_equation(equation):
    eqn = ''
    for relay in equation:
        eqn += ' + {} * {}'.format(round(equation[relay], 2), CTR_eqn[relay])
    return eqn

def format_constraints(constraint):
    for x in constraint:
        data = x
        data = data.split(' - ')
        primary = data[0]
        secondary = data[1]
        
        primary_arr = primary.split('*')
        secondary_arr = secondary.split('*')
        
        primary_trip = float(primary_arr[0])
        secondary_trip = float(secondary_arr[0])

        primary_relay = int(primary_arr[1].replace('(','').replace(')','').replace('x',''))
        secondary_relay = int(secondary_arr[1].replace('(','').replace(')','').replace('x',''))


        for y in range(1,15):
            if y == primary_relay:
                print(primary_trip, end=' ')
            elif y == secondary_relay:
                print( - secondary_trip, end= ' ')
            else:
                print(0, end=' ')
        print(';')
            

def format_additional_constraints(constraints):
    #9.85 * x(1)
    print('%%%%%%%%%%%%%%%%%')
    for x in constraints:
        data = x.split('*') 
        trip = float(data[0])
        relay_number = int(data[1].replace('(','').replace(')','').replace('x',''))
        for x in range(1,15):
            if x == relay_number:
                print(trip, end=' ')
            else:
                print(0, end=' ')
        print(';')
    print(len(constraints))

#===== calculation of tripping time ====   

def tripping_time(Isc, CTR, Ip):
    A = 0.14
    B = 0.02
    trip = A / ( ( (Isc * 1000 * (1/CTR ))/(5*Ip)   )**B - 1)
    return round(trip, 2)

#==== creating dictionary for better parseing ====

def create_dict(sheet):
    rows = sheet.rows
    SN = [x.value for x in next(rows)]
    json_data = {}
    print(SN)
    for x in range(12):
    # [1, 'R1', 2.431, 1, 'R12', 0.199, None, None, None, None]
    # [2, 'R2', 1.052, 1, 'R4', 1.052, None, None, None, None]     
    # [3, 'R3', 1.264, 1, 'R1', 1.264, None, None, None, None]     
        row = [x.value for x in next(rows)]
        json_data[row[1]] = { "current": row[2],
                                "backup":{
                                    "number": row[3], 
                                    "name": [x for x in row if 'R' in str(x) and row[1] != x ], 
                                    "backup_current":[x for x in row[4:] if isinstance(x, float) ] 
                                    } 
                            }
        print(json_data)
    return json_data

