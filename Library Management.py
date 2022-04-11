import os
import time
import random as rd
users={'Sethu':'1234','Kathir':'1234','Shantho Shree':'1234'}
us=['Shyam']
admin_his=list()
books = [{'name':'Phylophobia','count':4,'id':'USB1'},{'name':'Love Between India and Nepal','count':3,'id':'USB1'},{'name':'Shanthu Malavan','count':'1','id':'USB26'}]
def add_books():
    os.system('cls')
    b_nam = input("Enter the name of the Book -> ")
    b_cnt = int(input("Enter the Number of books to be stored -> "))
    b_id = 'USB'+str(rd.randint(10,100))
    books.append({'name':b_nam,'count':b_cnt,'id':b_id})
    input("\n\n Books Added Successfully....")
def add_count():
    os.system('cls')
    q=1
    for i in books:
        print(f"{q}) {i['name']} -> {i['count']} ")
        q+=1
    na = input("\nEnter the Name of the Book -> ")
    for i in books:
        if i['name']==na:
            co = int(input("\nEnter the Number of count of book -> "))
            i['count']+=co
            break
        else:
            print("The entered name of the book does not exist in database")
            break
    input("\n\n Books Count added Successfully....")
def remove_books():
    q=1
    for i in books:
        print(f"{q}) {i['name']}")
        q+=1
    na=input("\nEnter the Name of the to be removed ->")
    q=0
    no_count=0
    for i in books:
        if i['name']==na:
            books.pop(q)
            print("\t\tBook removed successfully....")
        if i['name']!=na:
            no_count+=1
        q+=1
    if no_count == len(books):
        print("\n\tNo Books Available....\n")
def view_books():
    q=1
    for i in books:
        print(f"\n{q}) Name -> {i['name']}\n Count -> {i['count']}\n Book ID -> {i['id']}" )
        print("\t  ------------------")
        q+=1
    input("\n\n Press Enter to Continue...")
def reports():
    q=1
    for i in admin_his:
        print(f"{q}) {i}")
        q+=1
    input("\n\n Press Enter to Continue....")
def new_user():
    new_name = input("\nEnter Name -> ")
    new_pass = input("\nEnter New Password -> ")
    if new_name in users:
        print("\n Name Already Exists...")
        input("\n\nPress Enter to Continue...")
    else:
        users.update({new_name:new_pass})
        us.append(new_name)
        print("\n User Created Successfully")
        input("\n\n Press Enter to Continue...")
class user:
    def __init__(self):
        self.book = list()
        self.cart = list()
    def add_cart(self,name):
        self.cart.append(name)
        input("\n\n Book added to cart...")
    def my_cart(self):
        q=1
        for i in self.cart:
            print(f"{q}) {i}")
            q+=1
        print("\n1) Checkout \n2) Remove Book \n3) Exit")
        choice = int(input("\nEnter your choice"))
        return choice
    def remove_cart(self):
        q=0
        na = input("\nEnter the name of the to be removed from the cart ->")
        for i in self.cart:
            if na==i:
                self.cart.pop(q)
                input("\n\nBook removed from cart successfully...")
            q+=1
    def checkout(self):
        na_count=0
        b_count=0
        for i in self.cart:
            if len(self.book)<2:
                self.book.append(i)
                admin_his.append(str(f"{name} Borrowed {i} Book from Library"))
                b_count+=1
            else:
                na_count+=1
        if na_count != 0:
            print("\n\tYou have already the limit of borrowing\n\tPlease Return the Books In time....")
            input("\nPress Enter to Continue....")
    def return_book(self):
        nas = input("Enter the Name of the book -> ")
        nai = input("Enter Book ID -> ")
        for i in books:
            if i['name']==nas and i['id']==nai:
                q=0
                for j in self.book:
                    if j==nas:
                        self.book.pop(q)
                        admin_his.append(str(f"{name} Returned {j} Book to library..."))
                        print("\n\tBook returned Successfully...\nThank You for using library..")
                    q+=1
        input("\n\n  Press enter to continue...")
    def search_book():
        na=input("\nEnter Name of book to search -> ")
        no_count = 0
        for i in books:
            if i['name']==na:
                print(f"\n\n\t Book Name : {i['name']}\n\t Book ID : {i['id']}\n\t No of BOoks available in Library : {i['count']}")
            else:
                no_count += 1
        if no_count == len(books):
            print("\n\n\t Book Not Available...")
        print("\n|n1) Add Bok to Cart\n2) Exit")
        choice = input("\nEnter you Choice -> ")
        return na,choice
while(True):        
    os.system('cls')
    print("\n\n\n\n\n\n\t\t\t\t\t\tWelcome to the National Library of United States of America")
    time.sleep(1.5)
    print("1) Admin \n2)User \n3)Exit\n")
    choice = int(input("\nEnter your choice -> "))
    if choice==3:
        print("Thank YOu for using the portal of USANL")
        break
    elif choice==2:
        os.system('cls')
        name = input("Enter your name -> ")
        password = input("Enter Password -> ")
        q=0
        for i in us:
            if i==name:
                a=q
            q+=1
        us[a] = user()
        if(name in users and password==user[name]):
            while(True):
                    os.system("cls")
                    print("\t   ---Welcome user---")
                    print("1) Search Books\n2) My Cart\n3) Return Books\n4) Logout")
                    choice = input("Enter Your Choice -> ")
                    if choice=='4':
                        break
                    elif choice=='3':
                        os.system("cls")
                        us[a].return_books()
                    elif choice=='2':
                        os.system("cls")
                        choice = us[a].my_cart()
                        if choice=='1':
                            os.system("cls")
                            us[a].checkout()
                        elif choice=='2':
                            us[a].remove_cart()
                        elif choice=='3':
                            continue
                        else:
                            input("\n\t  Invalid choice...")
                    elif choice=='1':
                        os.system("cls")
                        na,choice = search_book()
                        if choice=='2':
                            continue
                        elif choice=='1':
                            us[a].adding_cart(na)
                        else:
                            input("\n\t  Invalid choice...")
                    else:
                        input("\n\t  Invalid choice...")
            else:
                input("\n\n\t   Invalid Username or password...")    
        elif choice=='1':
            os.system("cls")
            new_user()
        else:
            input("\n\n\t   Invalid Choice...")
elif choice=='1':
    os.system("cls")
    ad = input("Enter Email -> ")
    pas = input("Enter Password -> ")
    if ad=='admin' and pas=='1234':
        while(True):
            os.system("cls")
            print("\t   ---Welcome Admin---\n")
            print("1) Add books\n2) Modify Book Counts\n3) Remove Books\n4) View Books\n5) Reports\n6) Exit\n")
            choice = input("Enter Your Choice -> ")
            if choice=='6':
                break
            elif choice=='5':
                os.system("cls")
                reports()
            elif choice=='4':
                os.system("cls")
                viewing_books()
            elif choice=='3':
                os.system("cls")
                removing_books()
            elif choice=='2':
                os.system("cls")
                adding_counts()
            elif choice=='1':
                os.system("cls")
                adding_books()
            else:
                input("\n\tInvalid Choice...")
    else:
        input("\n\n\t   Invalid Username or password...")            
else:
    input("\n\tInvalid Choice...")