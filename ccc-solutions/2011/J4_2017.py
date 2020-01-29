# Problem J4
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018

def tunnel_cords (input, pos):
    direction = input[0]
    steps = int(input[1])
    new_list = []
    new_list.append(pos)
    for i in range(steps):   
        print(pos)
        if direction == "l":
            pos[0]-=1
        if direction == "r":
            pos[0]+=1
        if direction == "u":
            pos[1]-=1
        if direction == "d":
            pos[1]+=1

        new_list.append(pos) 
        
    print(new_list)
        

pos = [[-1,-5]]
new = []

flag = False
while flag == False:

    movement = input().split()
    
    tunnel_cords(movement,pos[-1])

  
    






























# def create_matrix(a_list,rows,cols):
#     for rows in range(8):
#         a_list.append([])
#         for cols in range(13):
#             a_list[rows].append([])

#     return a_list

# def print_3d_list(inputs): #print a 3d list

#     for i in inputs:
#         print(i)
#     print('\n')

# well_plan = []

# well_plan = create_matrix(well_plan,8,13)

