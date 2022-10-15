#create the algorithm for the monte carlo method
import random as rd
import math as m

#create the function to calculate the area of the circle
def area_circle(x,y):
    return m.sqrt(x**2+y**2)

#create the function to calculate the area of the rectangle
def area_rectangle(x,y):
    return x*y

#create a circle and a rectangle
circle = {'x':0,'y':0,'r':1}
rectangle = {'x':0,'y':0,'w':1,'h':1}

#create the function that aleatorly generates the coordinates of the point inside the rectangle
def random_point_rectangle(rectangle):
    x = rd.uniform(-rectangle['w'],rectangle['w'])
    y = rd.uniform(-rectangle['h'] ,rectangle['h'])
    return x,y

#is the point inside the circle
def is_inside_circle(circle,point):
    return area_circle(circle['x']-point[0],circle['y']-point[1])<=circle['r']

#create list that will contain if the point is inside the circle or not
list_inside_circle = []
list_coordinates = []

while True:
   #create a point
    point=random_point_rectangle(rectangle)
    print("the coordinates of point are:",f"x: {point[0]} y: {point[1]}")

    pointInside = is_inside_circle(circle,point)
    #call the function is_inside_circle
    print('Is the point inside the circle?',pointInside)

    #add the point to the list
    list_inside_circle.append(pointInside)

    addpoint=[]
    if str(point[0])[0]!='-': #if no negative number add only the first 4 characters
        addpoint.append([str(point[0])[:4]]) 
    else: #if negative number add the first 5 characters
        addpoint.append([str(point[0])[:5]])

    if str(point[1])[0]!='-': 
        addpoint.append([str(point[1])[:4]])
    else:
        addpoint.append([str(point[1])[:5]])
    
    list_coordinates.append("("+str(addpoint[0])+","+str(addpoint[1])+")")

    #wait for the user to press enter
    next_action = input()
    if next_action=="1":
        #show the list of points
        print(list_inside_circle)
    elif next_action=="2":
        #show the list of coordinates
        for i in range(len(list_coordinates)):
            print(list_coordinates[i])
    elif next_action=="3":
        break

#random float in range
#rd.uniform(0,1)
#random float positive and negative in range
#rd.uniform(-1,1)

#raiz cuadrada
