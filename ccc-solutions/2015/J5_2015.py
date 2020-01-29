#CCC '15 J5 - π-day

visited = []

def pi(n,k,min):
    if visited [n][k][min] == 0:       
        if n == k:
            visited[n][k][min] = 1
        elif k == 1:
            visited[n][k][min] = 1
        else:
            t = 0
            for i in range (min, int(n / k)+1):
                t = t + pi(n-i, k-1, i)
            visited[n][k][min] = t
    return visited[n][k][min]


n = int(input())
k = int(input())

for i in range(n+1):
    x = []
    for j in range(k+1):
        t = []
        for kk in range(n+1):
            t.append (0)
        x.append(t)
    visited.append(x)

print (pi(n,k,1))
print(visited)
# def pi_days(pieces_of_pie, number_of_people, mini=1):

#     if pieces_of_pie == number_of_people or number_of_people == 1:
#         return 1
#     else:
#         result = 0
     
#         for i in range(mini,int(pieces_of_pie/number_of_people)+1):
#             result+=pi_days(pieces_of_pie-i,number_of_people-1,i)
#     return result

# print(pi_days(250,130))
