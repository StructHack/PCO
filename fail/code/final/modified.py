from openpyxl import load_workbook

def print_current():
    return 0

def create_eqn():
    book = load_workbook('BUS DATA MOD.xlsx')
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

    SN = [cell.value for cell in next(columns)][1:]
    line = [cell.value for cell in next(columns)][1:]
    fault_location = [cell.value for cell in next(columns)][1:]
    normal_current = [cell.value for cell in next(columns)][1:]
    fault_current = [cell.value for cell in next(columns)][1:]
    prim_relays = [cell.value for cell in next(columns)][1:]
    back_relays = [cell.value for cell in next(columns)][1:]
    prim_current_1 = [cell.value for cell in next(columns)][1:]
    prim_current_2 = [cell.value for cell in next(columns)][1:]
    back_current_1 = [cell.value for cell in next(columns)][1:]
    back_current_2 = [cell.value for cell in next(columns)][1:]
    back_current_3 = [cell.value for cell in next(columns)][1:]
    back_current_4 = [cell.value for cell in next(columns)][1:]

    for i in range(len(prim_relays)):
        # extracting the relay names
        relay_no = (prim_relays[i].split(","))
        back_relay_no = (back_relays[i].split(","))

        # relay names into variables
        r0 = relay_no[0].strip()
        r1 = relay_no[1].strip()

        if len(back_relay_no) == 2:
            #backup relay names
            b0 = back_relay_no[0].strip()
            b1 = back_relay_no[1].strip()
            #filling the dictionary
            relays[b0].append(back_current_1[i])
            relays[b1].append(back_current_2[i])
        else:
            #backup relay names
            b0 = back_relay_no[0].strip()
            b1 = back_relay_no[1].strip()
            b2 = back_relay_no[2].strip()
            b3 = back_relay_no[3].strip()
            #filling the directory
            relays[b0].append(back_current_1[i])
            relays[b1].append(back_current_2[i])
            relays[b2].append(back_current_3[i])
            relays[b3].append(back_current_4[i])
        
        #primary relays values are put in the dictionary
        relays[r0].append(prim_current_1[i])
        relays[r1].append(prim_current_2[i])
    
    return relays

relays = create_eqn()

for key in relays:
    A = 0.14
    B = 0.02
    CTR = 5
    Ip = 1.4
    for x in range(len(relays[key])):
        y = abs(float(relays[key][x])*1000) * (1200/5)
        relays[key][x]= A/(( ( y/(CTR*Ip))**B ) -1)

# for key in relays:
#     print("{},".format( sum(relays[key]), key ), end='')

# print(relays)