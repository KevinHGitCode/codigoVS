'''# in this file create a method that solve a simplex problem

#import 
from scipy.optimize import linprog

#create a method that solve a simplex problem
def simplex(c, A_ub, b_ub, A_eq, b_eq):
    #create a variable that will contain the result of the method
    result = linprog(c, A_ub, b_ub, A_eq, b_eq)
    #return the result
    return result

#call the method
result = simplex([1, 1], [[1, 1], [1, 1]], [2, 2], [[1, 1], [1, 1]], [2, 2])
#print the result
print("The result is: ")
print(result)'''

from scipy.optimize import linprog

c=[78,88,85]
A_ub=[[1,4,8],[40,30,20],[3,2,4]]
b_ub=[4500,36000,2700]
A_eq=[[1,1,1]]
b_eq=[999]
result = linprog(c, A_ub, b_ub, A_eq, b_eq,bounds=(0,None))
print("The result is: ")
print(result)

#linea de separacion
print("-----------------------------------------------------")
print("Valor optimo: ",result.fun,"\nX: ",result.x)
print("-----------------------------------------------------")

#segundo ejemplo
print("Segundo ejemplo: ")
c=[430,460,420]
A_ub=[[-1,-3,-1],[-2,0,-4],[-1,-2,0]]
b_ub=[-3,-2,-5]
result = linprog(c, A_ub, b_ub,bounds=(0,None))
print("The result is: ")
print(result)
print("-----------------------------------------------------")
print("Valor optimo: ",result.fun,"\nX: ",result.x)

