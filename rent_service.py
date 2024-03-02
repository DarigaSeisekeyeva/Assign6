import json
import csv 
import os
import sys
import string

#python main.py clean_goods
#python main.py clean_backup
#python main.py clean_database

class rentService:

    def create_database_files(self):
        
        if not os.path.exists("goods_database.txt"):
            open("goods_database.txt", "w").close()
        if not os.path.exists("backup_database.txt"):
            open("backup_database.txt", "w").close()


    def __init__(self):
        self.goods_list = []
        self.backup_goods_list = []
        self.create_database_files()
        self.load_data()


    def add_goods(self, name, description, price):

        try:
            price = float(price)
        except ValueError:
            print("Price must be a number")
            return

        if not 0 <= price <= 1000000:
            print("Price must be between 0 and 1000000")
            return

        goods = (len(self.goods_list) + 1, name, description, price)
        self.goods_list.append(goods)
        self.backup_goods_list.append(goods)
        self.save_data()
        self.save_to_backup()
        print("Goods added successfully!")


    
    def load_data(self):
        try:
            with open("goods_database.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 4:
                        goods = (int(parts[0]), parts[1], parts[2], float(parts[3]))
                        self.goods_list.append(goods)

        except FileNotFoundError:
            pass


    def save_data(self):
        with open("goods_database.txt", "w") as f:
            for goods in self.goods_list:
                f.write(f"{goods[0]}, {goods[1]}, {goods[2]}, {goods[3]}\n")



    def save_to_backup(self):
        with open("backup_database.txt", "w") as f:
            for goods in self.backup_goods_list:
                f.write(f"{goods[0]}, {goods[1]}, {goods[2]}, {goods[3]}\n")



    def search_goods(self, keyword):
        return [goods for goods in self.goods_list if keyword.lower() in str(goods.name).lower() or keyword.lower() in str(goods.description).lower()]
    #def search_goods(self, keyword):
        #return [goods for goods in self.goods_list if keyword.lower() in str(goods[1]).lower() or keyword.lower() in str(goods[2]).lower()]


    def save_to_json(self, filename):

        with open(filename, 'w') as f:
            json.dump([vars(goods) for goods in self.goods_list], f)


    def save_to_csv(self, filename):

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Registration', 'Name', 'Description', 'Price'])

            for goods in self.goods_list:
                writer.writerow([goods.registration, goods.name, goods.description, goods.price])



    def clean_database(self):

        confirmation = input("Are you sure you want to clean the database? (yes or no): ")
        if confirmation.lower() == 'yes':
            open("database.txt", "w").close()
            print("Database cleaned successfully!")
        else:
            print("Operation cancelled.")



    def clean_backup_database(self):

        confirmation = input("Are you sure you want to clean the backup database? (yes or no): ")
        if confirmation.lower() == 'yes':
            open("backup_database.txt", "w").close()
            print("Backup database cleaned successfully!")
        else:
            print("Operation cancelled.")



    def clean_goods_database(self):

        confirmation = input("Are you sure you want to clean the goods database? (yes or no): ")
        if confirmation.lower() == 'yes':
            open("goods_database.txt", "w").close()
            print("Goods database cleaned successfully!")
        else:
            print("Operation cancelled.")



    def delete_account(self):

        username = input("Enter username to delete account: ")
        with open("database.txt", "r") as db_file:
            lines = db_file.readlines()
        with open("database.txt", "w") as db_file:
            for line in lines:
                if not line.startswith(username):
                    db_file.write(line)

        print(f"Account '{username}' deleted successfully.")

    delete_account = delete_account



    
    def sell_goods(self):

        registration = int(input("Enter the registration number of the goods to sell: "))
        goods_to_sell = None
        for goods in self.goods_list:
            if goods[0] == registration:
                goods_to_sell = goods
                break

        if goods_to_sell is None:
            print("Goods not found.")
            return

        confirm = input(f"Are you sure you want to sell {goods_to_sell[1]} for {goods_to_sell[3]}? (y/n): ")
        if confirm.lower() != 'y':
            print("Sell operation cancelled.")
            return

        self.goods_list.remove(goods_to_sell)
        self.save_data()
        print(f"{goods_to_sell[1]} sold successfully!")


    sell_goods = sell_goods




    
    def register(self):

        username = input("Create username: ")
        password = input("Create password: ")
        password1 = input("Confirm password: ")



        if any(username in line for line in open("database.txt")):
            print("Username exists, please try again.")
            return False


        while password != password1 or len(password) <= 7 or not any(char.isdigit() for char in password) or not any(char in string.punctuation for char in password):

            if len(password) <= 7:
                print("Password too short, please try again.")

            elif not any(char.isdigit() for char in password):
                print("Password must contain at least one number.")

            elif not any(char in string.punctuation for char in password):
                print("Password must contain at least one special symbol.")

            else:
                print("Passwords do not match, please try again.")


            password = input("Create password: ")
            password1 = input("Confirm password: ")



        with open("database.txt", "a") as db:
            db.write(f"{username}, {password}\n")
        print("Registration successful!")
        return True




    def login(self):

        db = open("database.txt", "r")
        username = input("Enter your username: ")
        password = input("Enter your password: ")


        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))


        while True:
            try:
                
                if data[username]:
                    if password == data[username]:
                        print("Login success")
                        print("Hi, ", username)
                        break
                    else:
                        print("Password incorrect")
                        password = input("Enter your password again: ")
                else:
                    print("Username does not exist")
                    break
            except:
                print("Username does not exist")
                break





    def access(self):

        while True:
            option = input("Login | Signup: ")

            if option.lower() == "login":
                self.login()
            elif option.lower() == "signup":
                self.register()
            else:
                print("Please enter a valid option")

            
            if hasattr(self, 'logged_in') and self.logged_in:
                while True:
                    print("1. Add")
                    print("2. Search")
                    print("3. Logout")
                    number = input("Enter number: ")

                    if number == "1":
                        name = input("Name: ")
                        description = input("Description: ")
                        price = float(input("Price: "))
                        self.add_goods(name, description, price)

                    elif number == "2":
                        keyword = input("Keyword: ")
                        results = self.search_goods(keyword)
                        if results:
                            for goods in results:
                                goods.display()
                        else:
                            print("Nothing found")

                    elif number == "3":
                        print("Logout successful!")
                        self.logged_in = False
                        break

                    else:
                        print("Invalid input")

                continue

            break




    def run(self):

        if len(sys.argv) == 2:

            if sys.argv[1] == 'clean_goods':
                self.clean_goods_database()
            elif sys.argv[1] == 'clean_backup':
                self.clean_backup_database()
            elif sys.argv[1] == 'clean_database':
                self.clean_database()
            else:
                print("Invalid argument. Use 'clean_goods', 'clean_backup', or 'clean_database'.")
        else:

            while True:
                print("1. Add")
                print("2. Search")
                print("3. Clean goods database")
                print("4. Clean backup database")
                print("5. Clean main database")
                print("6. Logout")
                print("7. Delete account and end session")
                number = input("Enter number: ")


                if number == "1":
                    name = input("Name: ")
                    description = input("Description: ")
                    price = float(input("Price: "))
                    self.add_goods(name, description, price)


                elif number == "2":
                    keyword = input("Keyword: ")
                    results = self.search_goods(keyword)
                    if results:
                        for goods in results:
                            goods.display()
                    else:
                        print("Nothing found")


                elif number == "3":
                    self.clean_goods_database()
                    print("Goods database cleaned successfully!")

                elif number == "4":
                    self.clean_backup_database()
                    print("Backup database cleaned successfully!")

                elif number == "5":
                    self.clean_database()
                    print("Main database cleaned successfully!")
                    return
                    

                elif number == "6":
                    print("Logout successful!")
                    return 

                elif number == "7":
                    self.delete_account()
                    print("Account deleted.")
                    return

                elif number == "q":
                    break

                else:
                    print("Invalid input")


        def delete_account(self):
        
            pass



if __name__ == "__main__":
    rent_service = rentService()
    rent_service.run()
