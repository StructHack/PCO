import matplotlib.pyplot as plt
from openpyxl import load_workbook



def print_graph():
        
  
    # # our data
    book = load_workbook('BUS DATA.xlsx')
    sheet = book['bus_data']
    rows = sheet.rows
    cols = sheet.columns

    headers = [cell.value for cell in next(rows)]
    SN = [cell.value for cell in next(cols)][1:]
    bus_name = [cell.value for cell in next(cols)][1:]
    bus_type = [cell.value for cell in next(cols)][1:]
    voltage_mag = [cell.value for cell in next(cols)][1:]

    #reference data
    ref_sheet = book['ref_bus_data'] 

    ref_rows = ref_sheet.rows
    ref_cols = ref_sheet.columns

    ref_headers = [cell.value for cell in next(ref_rows)]
    ref_SN = [cell.value for cell in next(ref_cols)][1:]
    ref_bus_name = [cell.value for cell in next(ref_cols)][1:]
    ref_bus_type = [cell.value for cell in next(ref_cols)][1:]
    ref_voltage_mag = [cell.value for cell in next(ref_cols)][1:]


    # #plot
    font1 = {'family': 'serif', 'color':'black', 'size': 15}
    font2 = {'family': 'serif', 'color':'black', 'size': 10}

    plt.plot(SN, voltage_mag, linewidth=1, color='red', marker = 'x', ms=10, mec='red', mfc ='red')
    plt.plot(SN, ref_voltage_mag, linewidth=1,  marker = 'o', ms=5, mec='#2cbdfe', mfc ='#2cbdfe')

    plt.title('Voltage Magnitude plot', fontdict=font1)
    plt.xlabel('Bus number', fontdict = font2)
    plt.ylabel('Bus Voltage', fontdict = font2)


    plt.grid(color='green', linestyle='dotted', linewidth=0.5)
    plt.legend(['Voltage', 'reference voltage'], loc='lower left', fontsize=7)
    plt.show()
    #phase angle plot

    angle_mag = [cell.value for cell in next(cols)][1:]
    ref_angle_mag = [cell.value for cell in next(ref_cols)][1:]

    plt.plot(SN, angle_mag, linewidth=2, color='red', marker = 'x', ms=10, mec='red', mfc ='red')
    plt.plot(SN, ref_angle_mag, linewidth=1, color='#2cbdfe', marker = 'o', ms=5, mec='#2cbdfe', mfc ='#2cbdfe')

    plt.title('Phase Angle plot', fontdict=font1)
    plt.xlabel('Bus number', fontdict = font2)
    plt.ylabel('Phase angle magnitude', fontdict = font2)

    plt.grid(color='green', linestyle='dotted', linewidth=0.5)
    plt.legend(['Phase angle', 'Reference phase angle'], loc='lower left', fontsize=7)
    plt.show()
    #generation power plot

    power_mag = [cell.value for cell in next(cols)][1:]
    rpower_mag = [cell.value for cell in next(cols)][1:]
    ref_power_mag = [cell.value for cell in next(ref_cols)][1:]
    ref_rpower_mag = [cell.value for cell in next(ref_cols)][1:]

    
    plt.plot(SN, power_mag, linewidth=1, color='red', marker = 'x', ms=10, mec='red', mfc ='red')
    plt.plot(SN, ref_power_mag, linewidth=1, color='#2cbdfe', marker = 'o', ms=5, mec='#2cbdfe', mfc ='#2cbdfe')
    plt.plot(SN, rpower_mag, linewidth=1, color='yellow', marker = '*', ms=10, mec='yellow', mfc ='yellow')
    plt.plot(SN, ref_rpower_mag, linewidth=1, color='grey', marker = 'p', ms=5, mec='grey', mfc ='grey')
    

    plt.title('Generation power magnitude', fontdict=font1)
    plt.ylabel('Active/Reactive Power magnitude', fontdict=font2)
    plt.xlabel('Bus number', fontdict=font2)

    plt.grid(color='green', linestyle='dotted', linewidth=0.5)
    plt.legend(['AP', 'Reference AP', 'RP', 'Reference RP'], fontsize=7)

    plt.show()


    #load power plot
    lpower_mag = [cell.value for cell in next(cols)][1:]
    rlpower_mag = [cell.value for cell in next(cols)][1:]
    ref_lpower_mag = [cell.value for cell in next(ref_cols)][1:]
    ref_rlpower_mag =  [cell.value for cell in next(ref_cols)][1:]
    
    plt.plot(SN, lpower_mag, linewidth=1, color='red', marker = 'x', ms=10, mec='red', mfc ='red')
    plt.plot(SN, ref_lpower_mag, linewidth=1, color='#2cbdfe', marker = 'o', ms=5, mec='#2cbdfe', mfc ='#2cbdfe')
    plt.plot(SN, rlpower_mag, linewidth=1, color='yellow', marker = '*', ms=10, mec='yellow', mfc ='yellow')
    plt.plot(SN, ref_rlpower_mag, linewidth=1, color='grey', marker = 'p', ms=5, mec='grey', mfc ='grey')
    
    plt.title('Load power magnitude', fontdict=font1)
    plt.ylabel('Active/Reactive Power magnitude', fontdict=font2)
    plt.xlabel('Bus number', fontdict=font2)

    plt.grid(color='green', linestyle='dotted', linewidth=0.5)
    plt.legend(['AP', 'Reference AP', 'RP', 'Reference RP'], fontsize=7)
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.show()

    #short circuit analysis
    sheet = book['fault data']
    cols = sheet.columns
    SN = [cell.value for cell in next(cols)][1:]
    line = [cell.value for cell in next(cols)][1:]
    fault_location = [cell.value for cell in next(cols)][1:]
    normal_current = [cell.value for cell in next(cols)][1:]
    fault_current = [cell.value*1000 for cell in next(cols)][1:]
    plt.title('Fault Current Analysis', fontdict=font1)
    plt.ylabel('Current magnitude (A)', fontdict=font2)
    plt.xlabel('Line number', fontdict=font2)
   
    plt.grid(color='green', linestyle='dotted', linewidth=0.5)
    plt.plot(SN, normal_current,linewidth=1, color='red', marker = 'x', ms=10, mec='red', mfc ='red')
    plt.plot(SN, fault_current, linewidth=1, color='#2cbdfe', marker = 'o', ms=5, mec='#2cbdfe', mfc ='#2cbdfe')
    plt.legend(['Normal current','Fault current'])
    plt.show()