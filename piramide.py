import os
os.system("cls")

# n = int(input("Cuantos niveles quieres que tenga la piramide?"))
n = 10
for i in range(n):
    print((" ")*(i)+"*"*((n+n-i-1)-i))
# for i in range(n):
#     print()



for i in range(n):
    # print(" "*((((n//2)-i))-1)+"*"*(i+1)+" "*((((n//2)-i))-1))
    #1-3-5-7-11
    # print(" "*(n//2)+"*"*(i+1)+" "*(n//2))  #print mitad piramide
    # print("0"*((n-1)-i))
    print(" "*((n-1)-i)+("*"*((n+i)-(n-i)+1)))
# for i in range(n):
#     print()
# for i in range(n):
#     print("*"*((n+i)+1))

# for i in range(n):
#     print(("0"*(n-i)))

for i in range(n):
    print("*"*(i)+" "*(n-i)+" "*(n-i)+"*"*i)
for i in range(n):
    print("*"*(n-i)+" "*(i)+" "*(i)+"*"*(n-i))

for i in range(n):
    print("0"*(n-i)+"*"*(i)+"*"*(i)) 
for i in range(n):
    print("0"*(i)+"*"*(n-i)+"*"*(n-i))
