import pickle
import re


class AddressBook:
    @staticmethod
    def load_data():
        try:
            with open('data2.pickle', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_data(data):
        with open('data2.pickle', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def is_duplicate(data, email, mobile):
        for entry in data:
            if entry['email'] == email or entry['Mobile'] == mobile:
                return True
        return False

    @staticmethod
    def count_occurrences(data, field, value):
        count = 0
        for entry in data:
            if entry[field] == value:
                count += 1
        return count

    @staticmethod
    def count_occurrences_combined(data, fname=None, lname=None, street_address=None):
        count = 0
        if fname:
            count += AddressBook.count_occurrences(data, 'Fname', fname)
        if lname:
            count += AddressBook.count_occurrences(data, 'LName', lname)
        if street_address:
            count += AddressBook.count_occurrences(data, 'StreetAddress', street_address)
        return count

    @staticmethod
    def add_entry(fname, lname, street_address, city, state, country, mobile, email):
        data = AddressBook.load_data()
        if not AddressBook.is_duplicate(data, email, mobile) and re.match(r'^[6-9]\d{10}$', mobile):
            data.append({
                'Fname': fname,
                'LName': lname,
                'StreetAddress': street_address,
                'City': city,
                'State': state,
                'Country': country,
                'Mobile': mobile,
                'email': email
            })
            AddressBook.save_data(data)
            return True
        else:
            return False

    @staticmethod
    def main():
        attempts = 0
        while attempts <= 3:  # Corrected condition
            print("\n1. Add Entry")
            print("2. Find number of occurrences of a Fname")
            print("3. Find number of occurrences of a Lname")
            print("4. Find number of occurrences of a street")
            print("5. Find number of occurrences of Fname, Lname, and street combined")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                street_address = input("Enter Street Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                country = input("Enter Country: ")
                mobile = input("Enter Mobile: ")
                email = input("Enter Email: ")
                if AddressBook.add_entry(fname, lname, street_address, city, state, country, mobile, email):
                    print("Entry added successfully.")
                else:
                    print("Duplicate email or mobile number. Entry not added.")
            elif choice == '2':
                fname = input("Enter First Name to find occurrences: ")
                data = AddressBook.load_data()
                print("Occurrences of", fname, ":", AddressBook.count_occurrences(data, 'Fname', fname))
            elif choice == '3':
                lname = input("Enter Last Name to find occurrences: ")
                data = AddressBook.load_data()
                print("Occurrences of", lname, ":", AddressBook.count_occurrences(data, 'LName', lname))
            elif choice == '4':
                street_address = input("Enter Street Address to find occurrences: ")
                data = AddressBook.load_data()
                print("Occurrences of", street_address, ":",
                      AddressBook.count_occurrences(data, 'StreetAddress', street_address))
            elif choice == '5':
                fname = input("Enter First Name to find occurrences: ")
                lname = input("Enter Last Name to find occurrences: ")
                street_address = input("Enter Street Address to find occurrences: ")
                data = AddressBook.load_data()
                print("Occurrences of combined fields:",
                      AddressBook.count_occurrences_combined(data, fname, lname, street_address))
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
                attempts += 1

        else:
            print("Maximum attempts reached. Exiting...")


if __name__ == "__main__":
    AddressBook.main()
