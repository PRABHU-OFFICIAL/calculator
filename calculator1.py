import math

m=int(input("enter the first no. : "))

n=int(input("enter the second no. : "))

print("only plus , minus , multiply , divide , power , modulus , root ")

choice=input("enter the operations : ")

if (choice=="plus"):
    print(m+n)

if (choice=="minus"):
    print(m-n)

if (choice=="multiply"):
    print(m*n)

if (choice=="divide"):
    print(m/n)

if (choice=="modulus"):
    print(math.fmod(m,n))

if (choice=="root"):
    print(math.sqrt(m))

if (choice=="power"):
    print(math.pow(m,n))

else:
    print("invalid input")

print("operations finished")
