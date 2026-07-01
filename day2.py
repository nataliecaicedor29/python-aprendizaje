# métodos de strings:

frase = "Hi world, how are you?"
print (frase.upper())
print (frase.capitalize())
print (frase.replace("world" , "Colombia"))
print (len(frase))
print (frase.split(" "))

#operaciones matemáticas y f-strings:
cost = 50000
sale = 0.15 
final = cost - (cost * sale)
print(f"The final cost is: ${final:,.0f}")

#Mini reto: pide al usuario su nombre y año de nacimiento, calcula su edad y muestra un mensaje como:
#"Hola Ana, tienes 28 años y en 10 años tendrás 38"

name = input("What is your name? ")
age = int(input("What is yout age? "))
print("Hi", name + ", you are", age, "years old, and in ten years you will be", age + 10, "years old.")