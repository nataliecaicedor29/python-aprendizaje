import datetime


#Get data funtion
def get_data():
    name = input("Enter your full name ")
    city = input("Enter your city ")
    year = int(input("Enter your birth year: "))
    return name, city, year

#Calculate age funtion
def calculate_age(year):
    
    age = datetime.datetime.now().year - year 
    return age


#Classify age minor, young adult, adult  and senior
def classify_age(age):
    if age < 18:
        return "Minor"
    elif age >= 18 and age <= 25:
        return "Young adult"
    elif age >= 26 and age <= 64:
        return "Adult"
    else:
        return "Senior"

#Show information funtion
def show_gretting(name, city, age, classification):
     print (f"Hello {name}! You are {age} years old, from {city} and you are {classification}")
     
#Principal program
answer = "yes"
while answer == "yes":
    name, city, year = get_data()
    age = calculate_age(year)
    classification = classify_age(age)
    show_gretting(name, city, age, classification)
    
    answer = input("Do you want to analize another person? (yes/no) ")
    
    
        
    