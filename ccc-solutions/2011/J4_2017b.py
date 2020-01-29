# Problem J4
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018

import numpy

def flatten(input): #turns any 2d list into a 1d list
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list

def tunnel_cords (inp, pos):
    direction = inp[0]
    steps = int(inp[1])
    new_list = []

    for i in range(steps):
        if direction == "l":
            new_pos = [pos[0]-1,pos[1]]
        if direction == "r":
            new_pos = [pos[0]+1,pos[1]]
        if direction == "u":
            new_pos = [pos[0],pos[1]+1]
        if direction == "d":
            new_pos = [pos[0],pos[1]-1]

        new_list.append(new_pos)
        pos = new_pos
        
    return new_list
        

pos = [[-1,-5]]
cords_list = [[[-1,-5]]]

flag = False
while flag == False:

    movement = input().split()
    if movement[0] == "q":
        


    cords_list.append(tunnel_cords(movement,pos[-1]))
    
    
    pos = cords_list[-1]
    flat_cords_list = flatten(cords_list)

    for i in flat_cords_list:
        if  -3 > i[0] < 9: 
            print("{} danger".format(flat_cords_list[-1]))
            

            
        if -8>i[1]<-1: 
            print("{} danger".format(flat_cords_list[-1]))
           
          
    if flatten(flat_cords_list) == set(flatten(flat_cords_list)):
        print("{} danger".format(flat_cords_list[-1]))
                           





    else: print("{} safe".format(flat_cords_list[-1]))

    print(flat_cords_list)



   
