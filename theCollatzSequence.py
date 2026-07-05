def collatz(number):
    if number % 2 == 0: #Si es par
        number = number//2
        print(number)
        return(number)
    else:
        number = number*3 +1
        print(number)
        return (number)
        
number = int(input("Enter number: "))
while number != 1:
    number = collatz(number)
        