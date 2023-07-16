def factorial(n):
    if n <= 1:
        return 1
    else :
        return n*factorial(n-1)
    
nilai = input("n : ")
nilai = int(nilai)
print("Factorial dari "+str(nilai)+" adalah", factorial(nilai))