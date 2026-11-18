
#NOKIA 5510 MENU APP


#1. Phone book -
#2. Messages
#3. Chat
#4. Call register
#5. Tones
#6. Settings
#7. Call divert
#8. Music
#9. Games
#10. Calculator
#11. Reminders
#12. Clock
#13. Profiles
#14. Services
#15. SIM Services



def add_name():                    
    key = "1"
    while key !="0":
       
        new_name_number = input("Enter new contact number: ")
        new_name = input("Enter new contact name: ").capitalize()
        print("\n")
        validate_contact_new_number(new_name_number)
        validate_contact_new_name(new_name)
        break
       
    '''print(validate_contact_new_number(new_name_number))
    print(new_name_number)
    print(validate_contact_new_name(new_name))
    print(new_name)'''
    
    valid_number = validate_contact_new_number(new_name_number)
    valid_name = validate_contact_new_name(new_name)
    #print(valid_name)
    #print(valid_number)
    if valid_number == True and valid_number == True:
        contact_numberlist.append(new_name_number)
        contact_namelist.append(new_name)
    print("\n")
    key = input("To return to PHONE BOOK MENU (Press 0). \nTo continue (Press Any Key): ")
       
    return contact_namelist, contact_numberlist

def validate_contact_new_name(new_name):
    if len(new_name) <= 0:
        print("You can't submit a BLANK NAME")
        return False
         
    else:
        #print("Done")
        return True
                     
   

def validate_contact_new_number(new_name_number):
    if not new_name_number.isdigit():
        print("You entered an INVALID phone number!")
        return False
    elif len(new_name_number) != 11:
        print(f"\n{new_name_number} MUST contain 11 digits ONLY")
        return False
    else:
        #print("ok")
        return True
    
    
        

def search_name():                  
    search_name = input("Enter a name: ").capitalize()
    if search_name in contact_namelist:
        search_count = contact_namelist.index(search_name)
       
        search_number = contact_numberlist[search_count]
       
        #print(count)
        return search_name, search_number
    else:
        return f"{search_name} NOT FOUND!"
       
    #print(contact_namelist)
    #print(contact_numberlist)

def service_numbers():
    #print(service_numbers_dict)
    print("\n-----Service Numbers-----")
    for service, contact_of_service in service_numbers_dict.items():
       
        print(f"{service}: {contact_of_service}")
    print("-------------------------")
   
 
def display_contact():
    key = "1"
    serial_number = 1
    while key !="0":
        print("---**----YOUR PHONE BOOK DIRECTORY---**---")
        for saved_name, saved_number in zip(contact_namelist, contact_numberlist):
            print(f"{serial_number}. {saved_name}: {saved_number}")
            serial_number+=1
        print("---**----**---**---**---**---**---**---\n")
                    
        print("\n")
        key = input("To return to PHONE BOOK MENU (Press 0). \nTo continue (Press Any Key): ")




def erase():
    delete_choice = input("Press 1 to delete. Any key to return to Phone book: ")
    if delete_choice != "1":
        key = 0
    else:
        name_to_delete = input("Enter the name you wish to delete: ").capitalize()
        for name in contact_namelist:
            if name_to_delete in contact_namelist:
                name_to_delete_index = contact_namelist.index(name_to_delete)
                print(name_to_delete_index)
                return contact_namelist.remove(name_to_delete) 
            else:
                pass
        print(f"\n{name_to_delete} is not in your phone directory")
                
    
    
def edit():
    edit_choice = input("Press 1 to edit name. Press 2 to edit number. Any key to return to Phone book: ")
    #if edit_choice != "1" and edit_choice !=2:
        #key = 0
    if edit_choice == "1":
        name_to_edit = input("Enter the name you wish to edit: ").capitalize()
        updated_name = input("Input updated name: ").capitalize()
        if name_to_edit in contact_namelist:
            name_to_edit_index = contact_namelist.index(name_to_edit)
            contact_namelist[name_to_edit_index] = updated_name
        else:
            print(f"{name_to_edit} is not in your phone directory")
            #key = 0
        
    elif edit_choice == "2":
        number_to_edit = input("Enter the phone number you wish to edit: ")
        updated_number = input("Input updated number: ")
        if number_to_edit in contact_numberlist:
            number_to_edit_index = contact_numberlist.index(number_to_edit)
            contact_numberlist[number_to_edit_index] = updated_number
        else:
            print(f"{number_to_edit} is not in your phone directory")
            #key = 0
    else:
        key = 0




def phone_book():
   
    key = "1"
   
    while key !="0":
        print("\nPHONE BOOK MENU")
        print("_________________")
        print("Option 1: Search")
        print("Option 2: Service numbers")
        print("Option 3: Add name")
        print("Option 4: Erase")
        print("Option 5: Edit")
        print("Option 6: View contact")
        print("Option 0: Home Page")
        print("_________________")
        print("\n")
        key = input("Select your option: ")
        if key == "1":
            print(search_name())
            print("\n")
            key= input("Press 0 to exit phonebook menu. Press any key to continue: ")
            if key !="0":
                continue
            else:
                break
               
        elif key == "2":
            service_numbers()
            print("\n")
            key= input("Press 0 to exit phonebook menu. Press any key to continue: ")
            if key !="0":
                continue
            else:
                break
           
        elif key =="3":
            add_name()
       
        elif key =="4":
            erase()
       
        elif key =="5":
            edit()
        
        elif key =="6":
            display_contact()
        
        elif key =="0":
            break
           
        else:
            continue
   
    

def messages():
    pass

def chat():
    pass

def call_register():
    pass

def tones():
    pass

def settings():
    pass

def call_divert():
    pass

def music():
    pass

def games():
    pass

def calculator():
    pass

def reminders():
    pass

def clock():
    pass

def profiles():
    pass

def services():
    pass

def sim_services():
    pass


   
   
def home_page():
    key = "1"

    while key != "0":

   
        print("\n*****--HOME PAGE--*****")
        print("_________________________")
        print("Option 1: Phone Book")
        print("Option 2: Messages")
        print("Option 3: Chat")
        print("Option 4: Call Register")
        print("Option 5: Tones")
        print("Option 6: Settings")
        print("Option 7: Call Divert")
        print("Option 8: Music")
        print("Option 9: Games")
        print("Option 10: Calculator")
        print("Option 11: Reminders")
        print("Option 12: Clock")
        print("Option 13: Profiles")
        print("Option 14: Services")
        print("Option 15: SIM Services")
        print("Option 0: OFF")
        print("__________________________")
        print("\n")
       
       
        key = input("Select Your Option: ")
        if key != "0":
            if key == "1":
                phone_book()
            elif key == "2":
                messages()
            elif key == "3":
                chat()
            elif key == "4":
                call_register()
            elif key == "5":
                tones()
            elif key == "6":
                settings()
            elif key == "7":
                call_divert()
            elif key == "8":
                music()
            elif key == "9":
                games()
            elif key == "10":
                calculator()
            elif key == "11":
                reminders()
            elif key == "12":
                clock()
            elif key == "13":
                profiles()
            elif key == "14":
                services()
            elif key == "15":
                sim_services()
            else:
                continue
       
        else:
            print("GOOD BYE!")




contact_namelist = ["Emergency", "Bola", "Ade", "Emeka"]
contact_numberlist = ["111", "09093456724", "08086758903", "07075497901"]
service_numbers_dict = {"Customer Service": 100, "Fire Service": 200, "Security Service": 300}
key = "#"

while key == "#":

   
    print("**********__________WELCOME TO NOKIA 5510 MAIN MENU_________**********")
    print("\n")
   
    key = input("Press 0 to quit. Press any other key to continue: ")
    if key != "0":
        home_page()
   
    else:
        print("GOOD BYE!")

