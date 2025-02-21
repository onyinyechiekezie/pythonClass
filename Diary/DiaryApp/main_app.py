from diaries import Diaries
from my_diary import MyDiary

class MainApplication:
    def __init__(self):
        self.diaries = Diaries()
        self.my_diary = MyDiary("password","password")

        # MainApplication.run_app(self)

    def run_app(self):
        while True:
            print("""
                Welcome To Your Digital Diary. Write, Reflect and Grow With Us.
                Kindly choose an option:
                1. Create Diary
                2. Lock Diary
                3. Unlock Diary
                4. Create Entry
                5. Delete Entry
                6. Update Entry
                7. View Entry
                8. Delete Diary
                9. Exit
                """)

            option = input("Enter your choice: ")

            try:
                option = int(option)
                if option == 1:
                    self.create_diary()
                elif option == 2:
                    self.lock_diary()
                elif option == 3:
                    self.unlock_diary()
                elif option == 4:
                    self.create_entry()
                elif option == 5:
                    self.delete_entry()
                elif option == 6:
                    self.update_entry()
                elif option == 7:
                    self.view_entry()
                elif option == 8:
                    self.delete_diary()
                elif option == 9:
                    print("Thanks for using Onyii's diary")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def create_diary(self):
            user_name = input("Enter your Username: ")
            password = input("Enter your Password: ")
            self.diaries.add(user_name, password)
            print("Diary created")

    def lock_diary(self):
            if self.current_diary is None:
                print("No diary is unlocked. Please unlock a diary first.")
                return
            self.current_diary.lock_diary()
            print("Diary is locked")
            self.current_diary = None

    def unlock_diary(self):
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            diary = self.diaries.find_by_username(username)
            if diary and diary.unlock_diary(password):
                self.current_diary = diary
                print("Diary is unlocked")
            else:
                print("Invalid credentials or diary not found.")

self.MainApplication.run_app(MainApplication)


