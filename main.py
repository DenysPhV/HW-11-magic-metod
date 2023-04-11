import functools
from classes import * 
CONTACTS_ARRAY = AddressBook()

def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = False

        try:
            result = func(*args, **kwargs)
        except TypeError:
            print("""You have not entered all data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Denys 345-45-45)
for change please input:                    change name old tel. new tel.   (example: change Denys 234-57-89 584-25-12)
for reading please input:                   phone name         (example: phone Denys)
for delete number:                          delete name tel.   (example: phone Denys 345-45-45)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
        except IndexError:
            print("Invalid value. Try again.")
        return result
    return wrapper


def welcome_bot(func):
    def inner(*args, **kwargs):
        greeting = "\nWelcome to Assistant Console Bot\n"
        print("-"*(len(greeting)-2)+greeting+"-"*(len(greeting)-2))
        return func(*args, **kwargs)
    return inner

#add name and number in dict
@error_handler
def attach(name: str, number: str):
    user_name = Name(name)
    phone = Phone(number)
    rec:Record = CONTACTS_ARRAY.get(user_name.value)

    if rec:
        rec.add_phone_field(phone)
        return f"Phone number {phone} added successfully to contact {user_name}"
    
    rec = Record(user_name, phone)
    CONTACTS_ARRAY.add_record(rec)
    return f'Contact with name {name} and phone {number} add successful'
   

@error_handler
def delete(name: str, number: str):
    user_name = Name(name)
    phone = Phone(number)
    rec:Record = CONTACTS_ARRAY.get(user_name.value)

    if rec:
        return rec.delete_phone_field(phone)


@error_handler  # change number contact
def change(name: str, old_number:str, new_number: str):

    user_name = Name(name)
    old_number = Phone(old_number)
    new_number = Phone(new_number)
    rec:Record = CONTACTS_ARRAY.get(user_name.value)

    if old_number:
        return rec.change_phone_field(old_number, new_number)

    
# take phone from dict 
@error_handler
def get_phone(name: str):
    return COMMAND_ARRAY[name]


# ask get phone give phone by name
@error_handler
def show_phone(name: str):

    look_phone = get_phone(name)
    if look_phone: 
        return look_phone
    

# read dict with contact
def reader():
    if not CONTACTS_ARRAY:
        return "Your contact list is empty."
    return CONTACTS_ARRAY.show_all()

# say good bye and exit
@error_handler
def say_good_bye():
    return "Bye! Bye!"

def no_command(*args):
    return 'Unknown command. Try again'

COMMAND_ARRAY = {
    "hello": lambda: print("May I help you?"),
    "add": attach,
    "change": change,
    "delete": delete,
    "phone": show_phone,
    "show all":reader,
    'exit': say_good_bye,
	'bye': say_good_bye,
	'quit': say_good_bye,
	'close': say_good_bye,
	'.': say_good_bye
}


@error_handler
def parser(command):
    for key in COMMAND_ARRAY.keys():
        if command.startswith(key):
            new_line = command[len(key):].title()
            return COMMAND_ARRAY[key], new_line.split()
    return no_command, []
            

@ welcome_bot
def main():
    while True:
        user_input = input("Please enter your command: ").lower().strip()
        command, data = parser(user_input)
        
        print(command(*data))
        
        if command == say_good_bye:
            break

if __name__ == "__main__":
    main()
