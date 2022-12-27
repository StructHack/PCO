from helper import *

# helper has a function tripping time with tripping_time(Isc, CTR)
# CT has a function ct_ratio which gives the ct for all the relay ct_ratio()
#
#


def run():
    [objective, constraints, additional_constraints] = create_equation()
    objective_function = format_equation(objective)
    print('Objective function:::\n', objective_function, end='\n\n')
    print('PRIMARY - BACKUP CONSTRAINTS ==================')
    for x in constraints:
        print(f'0.3{x};...')
    # print('ADDITIONAL CONSTRAINTS =============')
    for x in additional_constraints:
        print(f'0.2-{x};...')
    
    # format_constraints(constraints)
    # format_additional_constraints(additional_constraints)
if __name__ == '__main__':
    run()