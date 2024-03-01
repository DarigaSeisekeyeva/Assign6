import json
import csv 



class rentService:

    def __init__(self):
        self.goods_list = []
        self.backup_goods_list = []


    def add_goods(self, name, description, price):

        goods = (len(self.goods_list) + 1, name, description, price)
        self.goods_list.append(goods)
        self.backup_goods_list.append(goods)


    def save_to_backup_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([vars(goods) for goods in self.backup_goods_list], f)


    def save_to_backup_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Registration', 'Name', 'Description', 'Price'])

            for goods in self.backup_goods_list:
                writer.writerow([goods[0], goods[1], goods[2], goods[3]])


    def search_goods(self, keyword):
        return [goods for goods in self.goods_list if keyword.lower() in str(goods[1]).lower() or keyword.lower() in str(goods[2]).lower()]


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
        confirmation = input("Are you sure you want to clean the database? (y/n): ")
        if confirmation.lower() == 'y':
            open("database.txt", "w").close()
            print("Database cleaned successfully!")
        else:
            print("Operation cancelled.")




    def register(self):

        db = open("database.txt", "r")
        username = input("Create username: ")
        password = input("Create password: ")
        password1 = input("Confirm password: ")

        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))


        while password != password1:

            print("Passwords do not match, please try again.")
            password = input("Create password: ")
            password1 = input("Confirm password: ")


        if len(password) <= 7:

            print("Password too short, please try again.")
            return False


        elif username in d:
            print("Username exists, please try again.")
            return False

        else:
            db.close()
            with open("database.txt", "a") as db:
                db.write(username + ", " + password + "\n")
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


        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login success")
                        print("Hi, ", username)
                    else:
                        print("Password incorrect")
                except:
                    print("Incorrect password or username")
            else:
                print("Username does not exist")
        except:
            print("Username does not exist")




    def access(self):

        option = input("Login | Signup: ")

        if option.lower() == "login":
            self.login()
        elif option.lower() == "signup":
            self.register()
        else:
            print("Please enter a valid option")




    def run(self):

        while True:
            
            print("1. Add")
            print("2. Search")
            print("3. End session")
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
                break

            else:
                print("Invalid input")