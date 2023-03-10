text = """(-3.169 * x(1)) + (-12.468 * x(12))
(-5.219 * x(2)) + (0.889 * x(4))  
(-0.865 * x(3)) + (4.575 * x(1))  
(-0.812 * x(4)) + (5.895 * x(6))  
(-0.812 * x(4)) + (10.207 * x(9)) 
(-0.812 * x(4)) + (5.527 * x(13)) 
(-2.983 * x(5)) + (0.943 * x(3))  
(-3.86 * x(6)) + (4.617 * x(8))   
(-2.983 * x(5)) + (19.556 * x(9)) 
(-2.983 * x(5)) + (4.03 * x(13))  
(-5.116 * x(7)) + (4.205 * x(5))  
(-3.187 * x(8)) + (-7.324 * x(10))
(-5.174 * x(9)) + (24.805 * x(7)) 
(-4.685 * x(10)) + (4.062 * x(13))
(-4.685 * x(10)) + (0.945 * x(3))
(-4.685 * x(10)) + (12.23 * x(6))
(-3.568 * x(11)) + (-11.779 * x(2))
(-5.907 * x(12)) + (3.284 * x(14))
(-2.533 * x(14)) + (9.635 * x(9))
(-3.072 * x(13)) + (5.265 * x(11))
(-2.533 * x(14)) + (1.0 * x(3))
(-2.533 * x(14)) + (5.697 * x(6))"""

new_text = text.split("\n")
for i in range(1,len(new_text)+1):
	eqn = new_text[i-1].split('+')
	for k in range(1,15):
		if k == int(eqn[0].split('*')[1].replace('x(','').replace(')','')):
			print(float(eqn[0].split('*')[0].strip().replace('(','')),end=' ')
		elif  k == int(eqn[1].split('*')[1].replace('x(','').replace(')','')):
			print("{}".format(float(eqn[1].split('*')[0].strip().replace('(',''))),end=' ')
		else:
			print(0,end=' ')
	print(';')