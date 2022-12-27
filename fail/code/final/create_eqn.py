import xdrlib
from openpyxl import load_workbook

def tripping_time(x, ctr):
    A = 0.14
    B = 0.02
    CTR = 5
    Ip = 1.4
    y = abs(float(x)*1000) * ctr
    return round(A/(( ( y/(CTR*Ip))**B ) -1),3)

def create_eqn():
    book = load_workbook('BUS DATA.xlsx')
    sheet = book['fault data']
    columns = sheet.columns

    relays = {
        'R1':[],
        'R2':[],
        'R3':[],
        'R4':[],
        'R5':[],
        'R6':[],
        'R7':[],
        'R8':[],
        'R9':[],
        'R10':[],
        'R11':[],
        'R12':[],
        'R13':[],
        'R14':[]
    }

    CT = {
    'R1': 600/5,
    'R2': 600/5, 
    'R3': 200/5, 
    'R4': 600/5, 
    'R5': 600/5, 
    'R6': 200/5, 
    'R7': 200/5, 
    'R8': 600/5, 
    'R9': 200/5, 
    'R10': 600/5,
    'R11': 600/5,
    'R12': 150/5,
    'R13': 200/5,
    'R14': 600/5,
}

    SN = [cell.value for cell in next(columns)][1:]
    line = [cell.value for cell in next(columns)][1:]
    fault_location = [cell.value for cell in next(columns)][1:]
    normal_current = [cell.value for cell in next(columns)][1:]
    fault_current = [cell.value for cell in next(columns)][1:]
    prim_relays = [cell.value for cell in next(columns)][1:]
    back_relays = [cell.value for cell in next(columns)][1:]
    prim_current_1 = [cell.value for cell in next(columns)][1:] #primary current 1 for R1
    prim_current_2 = [cell.value for cell in next(columns)][1:] #primary current for R2
    back_current_1 = [cell.value for cell in next(columns)][1:] # Backup current R4
    back_current_2 = [cell.value for cell in next(columns)][1:] #Backup current R12
    back_current_3 = [cell.value for cell in next(columns)][1:]
    back_current_4 = [cell.value for cell in next(columns)][1:]

    for i in range(len(prim_relays)):
        # extracting the relay names
        relay_no = (prim_relays[i].split(",")) # ['R1', ' R2']
        back_relay_no = (back_relays[i].split(",")) #['R12', 'R4']

        # primary relay names into variables R1, R2
        r0 = relay_no[0].strip() #r0 = R1
        r1 = relay_no[1].strip() #r1 = R2
        
        if len(back_relay_no) == 2:
            #backup relay names

            b0 = back_relay_no[0].strip() # R12
            b1 = back_relay_no[1].strip() #R4
            #filling the dictionary
            relays[b0].append(back_current_1[i]) #appending to the dictionary
            relays[b1].append(back_current_2[i])
            #creating constraints
            print("({} * x({})) + ({} * x({}))".format(-tripping_time(prim_current_1[i], CT[r0]),r0[1:],tripping_time(back_current_1[i], CT[b0]),b0[1:]))
            print("({} * x({})) + ({} * x({}))".format(-tripping_time(prim_current_2[i], CT[r1]),r1[1:],tripping_time(back_current_2[i], CT[b1]),b1[1:]))
        else:
            #backup relay names
            b0 = back_relay_no[0].strip() #R1+
            b1 = back_relay_no[1].strip() #R6*
            b2 = back_relay_no[2].strip() #R9*
            b3 = back_relay_no[3].strip() #R12*
            #filling the directory
            relays[b0[:-1]].append(back_current_1[i])
            relays[b1[:-1]].append(back_current_2[i])
            relays[b2[:-1]].append(back_current_3[i])
            relays[b3[:-1]].append(back_current_4[i])
            #constraints
            backup_current = [back_current_1[i],back_current_2[i],back_current_3[i],back_current_4[i]]
            for x in range(len(backup_current)):
                if back_relay_no[x].strip()[-1:] == '+':
                   print("({} * x({})) + ({} * x({}))".format(-tripping_time(prim_current_1[i], CT[r0]),r0[1:],tripping_time(backup_current[x], CT[back_relay_no[x].strip()[:-1]]),back_relay_no[x].strip()[:-1][1:]))
                else:
                    print("({} * x({})) + ({} * x({}))".format(-tripping_time(prim_current_2[i],CT[r0]),r1[1:],tripping_time(backup_current[x], CT[back_relay_no[x].strip()[:-1]]),back_relay_no[x].strip()[:-1][1:]))

            
        #primary relays values are put in the dictionary
        relays[r0].append(prim_current_1[i])
        relays[r1].append(prim_current_2[i])
    
    return relays

relays = create_eqn()

for key in relays:
    CT = {
    'R1': 600/5,
    'R2': 600/5, 
    'R3': 200/5, 
    'R4': 600/5, 
    'R5': 600/5, 
    'R6': 200/5, 
    'R7': 200/5, 
    'R8': 600/5, 
    'R9': 200/5, 
    'R10': 600/5,
    'R11': 600/5,
    'R12': 150/5,
    'R13': 200/5,
    'R14': 600/5,
}

    A = 0.14
    B = 0.02
    CTR = 5
    Ip = 1.2
    for x in range(len(relays[key])):
        y = float(relays[key][x])*1000 / CT[key]
        relays[key][x]= round(A/abs(( ( y/(CTR*Ip))**B ) -1),3)

print(relays)
# for key in relays:
#     print("{} * x({})".format( round(sum(relays[key]),3), key[1:] ), end='+')
