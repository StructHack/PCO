from openpyxl import load_workbook
from constants import *


def trip(Isc, CTR, Ip):
    A = 0.14
    B = 0.02
    Isc = Isc * 1000
    Deno = (Isc / CTR) / (5 * Ip) 
    
    try:
        TripTime = A / ((Deno ** B)-1)
    except ZeroDivisionError:
        print(f'Zero Division occured due to {Isc} {CTR} {Ip}')
        return
    
    return round(TripTime, 2)

def create_dict(sheet):
    Rows = sheet.rows
    Sn = [x.value for x in next(Rows)]
    Json = {}
    print(Sn)
    for i in range(7):
        DataOne = [x.value for x in next(Rows)]
        DataTwo = [x.value for x in next(Rows)]
        print(DataOne)
        print(DataTwo)
        RelayName = DataOne[1]
        Json[RelayName] = {
            'first': {
                'primary_current': DataOne[2],
                'backup':{
                    'number': DataOne[3],
                    "name": [x for x in DataOne if 'R' in str(x) and DataOne[1] != x ], 
                    "backup_current":[x for x in DataOne[4:] if isinstance(x, float) ] 
 
                }
            },
            'second':{
                'primary_current': DataTwo[2],
                'backup':{
                    'number': DataTwo[3],
                    "name": [x for x in DataTwo if 'R' in str(x) and DataTwo[1] != x ], 
                    "backup_current":[x for x in DataTwo[4:] if isinstance(x, float) ] 
 
                }
            }
        }
    
    return Json


def excel_conversion():
    Book = load_workbook('Book1.xlsx')
    Sheet = Book['FinalData']
    Json = create_dict(Sheet)
    create_constraints(Json)
    
def create_constraints(Json):
    for x in Json:
        PrimRelay = x 
        PrimCurrent = Json[PrimRelay]['first']['primary_current']
        PrimCurrentTwo = Json[PrimRelay]['second']['primary_current']
        PrimTrip = trip(PrimCurrent, CTR[PrimRelay], IP[PrimRelay])
        PrimTripTwo = trip(PrimCurrentTwo, CTR[PrimRelay], IP[PrimRelay])
        BackupNo = int(Json[PrimRelay]['first']['backup']['number'])
        for y in range(BackupNo):
            BackupName = Json[PrimRelay]['first']['backup']['name'][y]
            BackupCurrent = Json[PrimRelay]['first']['backup']['backup_current'][y]
            BackupTrip = trip(BackupCurrent, CTR[BackupName], IP[BackupName])
            
            BackupNameTwo = Json[PrimRelay]['second']['backup']['name'][y]
            BackupCurrentTwo = Json[PrimRelay]['second']['backup']['backup_current'][y]
            BackupTripTwo = trip(BackupCurrentTwo, CTR[BackupNameTwo], IP[BackupNameTwo])


            print(f'0.3-{BackupTrip}*{CTR_eqn[BackupName]}+{PrimTrip}*{CTR_eqn[PrimRelay]};...')
            print(f'0.3-{BackupTripTwo}*{CTR_eqn[BackupNameTwo]}+{PrimTripTwo}*{CTR_eqn[PrimRelay]};...')





if __name__ == '__main__':
    print(excel_conversion())