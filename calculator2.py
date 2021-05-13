import math

def calculator( m , n):
    c = 0
    choice = input("enter the operations : ")

    if (choice == "plus"):
        print("The sum is : ")
        c = m + n

    if (choice == "minus"):
        print("The difference is : ")
        c = m - n

    if (choice == "multiply"):
        print("The product is : ")
        c = m * n

    if (choice == "divide"):
        print("The quotient is : ")
        c = m / n

    if (choice == "modulus"):
        c = math.fmod(m , n)

    if (choice == "root"):
        c = math.sqrt(m)

    if (choice == "power"):
        c = math.pow(m , n)

    if (m < 0 or n < 0):
        print(" invalid statement")

    return c

m = int(input("enter the first no. : "))

n = int(input("enter the second no. : "))

print("only plus , minus , multiply , divide , power , modulus , root ")

print(calculator(m, n))

print("operations finished")
