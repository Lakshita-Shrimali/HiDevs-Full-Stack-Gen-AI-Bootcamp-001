import pickle


class PersonalInfoManager:
    @staticmethod
    def load_data():
        try:
            with open('data1.pickle', 'rb') as f:
                personal_info = pickle.load(f)
        except FileNotFoundError:
            personal_info = {}    #initialize with an empty dictionary if file not exists
        return personal_info

    @staticmethod
    def main():
        personal_info = PersonalInfoManager.load_data()
        attempts = 0
        while attempts < 3:
            try:
                print("1. Enter new name and date of birth")
                print("2. Search for name and display date of birth")
                print("3. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    name = input("Enter name: ")
                    dob = input("Enter date of birth (YYYY-MM-DD): ")
                    secret_input = input("Is the date of birth secret? (yes/no): ").lower()
                    secret = secret_input.lower() == 'yes'
                    personal_info[name] = {'dob': dob, 'secret': secret}
                    PersonalInfoManager.save_data(personal_info)
                elif choice == '2':
                    name = input("Enter name to display DOB: ")
                    dob_info = personal_info.get(name)
                    if dob_info:
                        if dob_info['secret']:
                            print("Date of birth for", name, "is secret.")
                        else:
                            print("Date of birth for", name, "is", dob_info['dob'])
                    else:
                        print("Name not found.")
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please choose again.")
                    attempts += 1
                    #print(attempts)

            except Exception as e:
                print("Error:", e)

        else:
            print("Maximum attempts reached. Exiting..")

    @staticmethod
    def save_data(personal_info):
        with open('data1.pickle', 'wb') as f:
            pickle.dump(personal_info, f)

if __name__ == "__main__":
    PersonalInfoManager.main()
