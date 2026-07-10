#For, while, break y continue
#Loops
fruits = ["mango", "banana","apple"]

for fruit in fruits:
    print(f"I like the {fruit}")

for i in range(1, 6):
    print(f"Semana {i} del plan")

#Menu 
while True:
    opcion = input(" 1. Saludar 2. Salir")
    if opcion == "1":
        print("Hello!")
    elif opcion == "2":
        print("Good bye!")
        break