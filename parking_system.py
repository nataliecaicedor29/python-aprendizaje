#Parking system

import datetime
import os
import math

#Total Spots (1 to 10)
total_spots = 10
#Available spots 
available_spots = list(range(1,11))
# Vehicles inside {plate: {spot, entry_time}}
vehicles = {}
#Funtions
def register_entry():
    #Verifi paking full
    if len(vehicles) == total_spots:
        print("Parking is full!")
        return
    plate = input("Enter plate: ").upper() #ABC=abc
    # Validate plate length (must be 6 characters)
    while len(plate) != 6:
        print("Invalid plate! Must be 6 characters (example: ABC123)")
        plate = input("Enter plate: ").upper()
    # Validate plate is not already inside
    if plate in vehicles:
        print(f"Vehicle {plate} is already inside!")
        return
    #Assing firts available spot, use "pop(0)"
    # pop(0) takes the first spot from the list and removes it
    spot = available_spots.pop(0) 
    #Get current time
    entry_time = datetime.datetime.now()
    
    # Save vehicle in dictionary
    vehicles[plate] = {"spot": spot, "entry_time": entry_time}
    # Confirm entry
    print(f"Vehicle {plate} is assigned to spot {spot}")
    
def register_exit():
    plate = input("Enter plate: ").upper() 
    if plate not in vehicles:
        print(f"The vehicle is not in the parking")
        return
    exit_time = datetime.datetime.now()
    entry_time = vehicles [plate]["entry_time"]
    time_parking = exit_time - entry_time
    hours = time_parking.total_seconds() / 3600
    hours = math.ceil(hours)
    cost = hours*2000
    print (f"Vehicle: {plate}")
    print (f"Hours parked: {hours}")
    print (f"Total cost: $ {cost}")
    available_spots.append(vehicles[plate]["spot"])
    del vehicles[plate]

def show_available_spots():
    print("\nAvailable spots:", available_spots)
    print("Occupied:", len(vehicles), "of", total_spots)
    input("Press Enter to continue...")
    
def show_vehicles():
    #Check if parking is empty
    if len(vehicles) == 0:
        print("Parking is empty!")
        return
    print("\n--- Vehicles inside ---")
    for plate, data in vehicles.items():
        print(f"Plate: {plate} | Spot: {data['spot']} | Entry: {data['entry_time']}")
         
#Menu
def main():
    while True:
        print("\n=== PARKING SYSTEM ===")
        print("1. Register vehicle entry")
        print("2. Register vehicle exit")
        print("3. Show available spots")
        print("4. Show all vehicles inside")
        print("5. Exit")
        
        option = input("Choose an option: ")
        if option == "1":
            register_entry()
        elif option == "2":
            register_exit()
        elif option == "3":
            show_available_spots()
            os.system('pause')
        elif option == "4":
            show_vehicles()
        elif option == "5" :
            print("Goodbye!")
            break
        else:
            print ("Invalid option!")
main()