from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
         if not value:
              raise ValueError("Name cannot be empty")
         super().__init__(value)

class Phone(Field):
    def __init__(self, value):
         if not self._validate_phone(value):
             raise ValueError("Phone number must be 10 digits")
         super().__init__(value)

    def _validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                break

    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone:
                if not Phone(new_phone)._validate_phone(new_phone):
                    raise ValueError("New phone number must be 10 digits")
                i.value = new_phone
                break

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None

    def __str__(self):
        phones_str = "; ".join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
	
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")

book.delete("Jane")

jane = book.find("Jane")
print(jane)