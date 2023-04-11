from collections import UserDict
import datetime
from itertools import islice

class Field:
    def __init__(self, value: str):
        self.value = value

    # add for hw 11
    def __str__(self) -> str:
        return f"{self.value}"
    # add for hw 11
    def __repr__(self) -> str:
         return f"{self.value}"

# add for hw 11
class Birthday(Field):

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, val: str):
        data = val.split("-")

        if not "".join(data).isdigit():
            raise ValueError

        if int(data[0]) > datetime.now().year or int(data[1]) > 12 or int(data[2]) > 30:
            raise ValueError
        self.value = val

class Name(Field):
    pass

class Phone(Field):
    # add for hw 11
    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, val: str):
        if not len(val) == 10 and not len(val) == 13 and not val.lstrip('+').isdigit():
            raise ValueError

        if len(val) == 10:
            val = "+38" + val

        if not val[3] == "0":
            raise ValueError
        self.value = val


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phones = []
        self.birthday = birthday # add for hw 11
    
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

# add for hw 11
    def days_to_birthday(self):
        if not self.birthday.value:
           print("Birthday not entered")
        else:
            date_first = self.birthday.value.split("-")
            date = datetime(year=datetime.now().year, month=int(date_first[1]), day=int(date_first[2]))
            date_now = datetime.now()
            dat = date - date_now
            return dat.days

     
class AddressBook(UserDict):
    index = 0 # add for hw 11

    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec
    
    def show_all(self):
        return '\n'.join([f'{r.name.value} : {",".join([str(p) for p in r.phones])}' for r in self.data.values()])
   
    # add for hw 11
    def iteration(self, step=5):
        while AddressBook.index < len(self):
            yield list(islice(self.items(), AddressBook.index, AddressBook.index+step))
            if AddressBook.IndentationError > len(self):
                raise StopIteration()
            AddressBook.index += step