#I create the diccionary 
contacts = {}
#Functions
def add_contact():
    name = input("Write the name: ")
    phone_number = input("Write the phone number: ")
    while not phone_number.isdigit() or len(phone_number) != 10:
        print("Invalid! Must be 10 digits.")
        phone_number = input("Write the phone number: ")
    mail = input("Write the mail: ")
    while "@" not in mail or "." not in mail:
        print("Invalid email!")
        mail = input("Write the mail: ")  
    address = input("Write the address: ")
    occupation = input("Write the occupation: ")

    contacts[phone_number] = {"name": name, "mail": mail, "address": address, "occupation": occupation}
    print(f"Contact {name} added successfully!")
    input("Press Enter to continue...")
    
def delete_contact():
    phone_number = input("Enter the phone number you wish to delete ")
    if phone_number not in contacts:
        print(f"The phone number doesn't exist")
        return
    del contacts[phone_number]
    print(f"The contact {phone_number} was deleted")
    
def search_contact():
    name = input("Enter the name ")
    found = False
    for phone_number, data in contacts.items():
        if data ['name'].lower() == name.lower():
            print(f"Phone number: {phone_number} | Name: {data['name']} | mail: {data['mail']} | address: {data['address']} | occupation: {data['occupation']}")
            found =True
    if not found:
        print("Contact not found!")
def show_contacts():
    if len(contacts) == 0:
        print("The contact book is empty!")
        return
    for phone_number, data in contacts.items():
        print(f"Phone number: {phone_number} | Name: {data['name']} | mail: {data['mail']} | address: {data['address']} | occupation: {data['occupation']}")
    input("Press Enter to continue...")
        
#Menu
def main():
    #Principal menu
    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Show contacts")
        print("5. Exit")
        
        option = input ("Choose an option: ")
        if option == "1":
            add_contact()
        elif option == "2":
            delete_contact()
        elif option == "3":
            search_contact()
        elif option == "4":
            show_contacts()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose an option")
    

main() 