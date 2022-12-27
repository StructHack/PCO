%% main code for minimizing the fitness function using GA

ObjFcn = @myFitness;
nvars = 14;
LB = zeros(1,14) + 0.05;
UB = zeros(1,14)+5;
constraintfunc = @constraint;
[x,fval,exitflag,output,population,scores] = ga(ObjFcn, nvars,[],[],[],[], LB, UB,constraintfunc,[]);


