%% Constraint function
function [c, c_eq] =  myConstraints(x)
 c = [-0.6300363046613873 * x(1) + 0.6472633395821413 * x(12) +0.2;
-0.6126386304637192 * x(2) + 0.6126386304637192 * x(4) +0.2;   
-0.6906751014443325 * x(3) + 0.6906751014443325 x(1) + 0.2;    
-0.5790522236775913 * x(4) + 0.6233442123650259 * x(6) + 0.2;  
-0.5790522236775913 * x(4) + 0.6099451028842652 * x(9) + 0.2;  
-0.5790522236775913 * x(4) + 0.7462119119126829 * x(13) + 0.2; 
-0.6060703987328993 * x(5) + 0.8398139888447852 x(3) + 0.2;    
-0.5944969844680665 * x(6) + 0.5944969844680665 * x(8) + 0.2;  
-0.6060703987328993 * x(5) + 0.6162835774825137 x(9) + 0.2;    
-0.6060703987328993 * x(5) + 0.8295528047566095 x(13) + 0.2;   
-0.6609915936595411 * x(7) + 0.6609915936595411 * x(5) +0.2;   
-0.5594702589789741 * x(8) + 0.6890393830558672 * x(10) +0.2;  
-0.5792957595016371 * x(9) + 0.6373689462992375 x(7) + 0.2;    
-0.6230663075003706 * x(10) + 0.8279486782146901 * x(13) + 0.2;
-0.6230663075003706 * x(10) + 0.8380228267604467 * x(3) + 0.2; 
-0.6230663075003706 * x(10) + 0.6373689462992375 * x(6) + 0.2;
-0.635734774679531 * x(11) + 0.655159740444625 * x(2) +0.2;
-0.6073083514944438 * x(12) + 0.6073083514944438 * x(14) +0.2;
-0.5762952145066845 * x(14) + 0.6040026071011245 * x(9) + 0.2;
-0.69825931745625 * x(13) + 0.69825931745625 x(11) + 0.2;
-0.5762952145066845 * x(14) + 0.716500264821008 * x(3) + 0.2;
-0.5762952145066845 * x(14) + 0.6228817914611201 * x(6) + 0.2;];
 c_eq = [];
end