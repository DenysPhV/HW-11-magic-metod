from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self) -> str:
        return self.value

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
    
        if phone:
            self.phones.append(phone)

    def add_phone_field(self, phone_number: Phone):
        self.phones.append(phone_number)
   
        
    def delete_phone_field(self, phone_number: Phone):
        for i in self.phones:
            if i.value == phone_number.value:
                self.phones.remove(i)
                return f'Phone {i.value} delete successful.'
            return f'Phone {phone_number.value} not found'


    def change_phone_field(self, old_number: Phone, new_number: Phone):
        for i, p in enumerate(self.phones):
            if p.value == old_number.value:
                self.phones[i] = new_number
                return f"Phone {old_number.value} changed on {new_number.value}"
        return f"Contact does not contain such phone number: {old_number}"
    
     
class AddressBook(UserDict):

    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec
    
    def show_all(self):
        return '\n'.join([f'{r.name.value} : {",".join([str(p) for p in r.phones])}' for r in self.data.values()])