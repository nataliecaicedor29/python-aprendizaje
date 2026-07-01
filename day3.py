#Programa de edad con if
age = int(input("What is your age"))
if age <18: 
    print ("You are minor")
elif age >= 65:
    print ("You are older")
else: 
    print ("You are adult")

#programa que pida una nota (0-100) y muestre si es: 
#Reprobado / Aprobado / Bueno / Excelente

grade = int(input("Please enter you grade (0 to 100): "))
if grade <0 or grade >100:
    print ("Invalid grade. Please enter a value between 0 and 100.")
else:
    if grade <= 59:
        print ("FAILED")
    elif grade < 80 and grade >= 60: 
        print ("PASSED")
    elif grade < 90 and grade >=80:
        print ("GOOD")
    elif grade <= 100 and grade >=90:
        print ("EXCELENT")
        
#Operadores lógicos

exp = False
port = True
if not exp and port:
    print ("Apply anyway—your portfolio speaks for itself!")
    
