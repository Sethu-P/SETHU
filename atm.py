import time
import os
os.system('cls')
atm_balance = 140000
account_balance = 10000
notes={'2000':40,'500':40,'200':100,'100':200}
notes1={'2000':0,'500':0,'200':0,'100':0}
def admin():
    global atm_balance
    time.sleep(1)
    print("The admin panel environment is being running....\nPlease wait for some time")
    time.sleep(1)
    a=int(input("\n1.Loading Currency \n2.Check for Balance \n3.Exit\n"))
    time.sleep(1)
    if a==1:
          print("\n")
          l = notes.get('2000') + int(input("Enter the Number of Rs.2000 notes : "))
          m = notes.get('500')  + int(input("Enter the Number of Rs.500  notes : "))
          n = notes.get('200')  + int(input("Enter the Number of Rs.200  notes : "))
          o = notes.get('100')  + int(input("Enter the Number of Rs.100  notes : "))
          notes.update({'2000':l, '500':m, '200':n, '100':o})
          time.sleep(1)
          print("\nLATEST BALANCE STATUS")
          for key,value in notes.items():
              print("INR",key,"- No. of notes : ",value)
          atm_balance = (2000*notes.get('2000')) + (500*notes.get('500')) + (200*notes.get('200')) + (100*notes.get('100'))
          time.sleep(1)
          print("\nTotal Indian National Rupees Reserve in this ATM/CDM is Rs.: ",atm_balance)
    elif a==2:
        for key,value in notes.items():
            print("INR",key,"- No. of notes : ",value)
            time.sleep(1)
        time.sleep(0.5)
        print("\nThe Current Currency Reserve in this ATM/CDM is INR :",atm_balance)
    time.sleep(3)
    print("\n\nPress 1\tIf you wish to continue the process?\nPress 2\tExit")
    time.sleep(1)
    z=int(input())
    if z==1:
        admin()
    else:
        print("\nThank You for your Service..")
def user():
    global atm_balance
    global account_balance
    os.system('cls')
    time.sleep(1)
    print("\nUnion Bank of Switzerland Proudly Welcomes You..")
    time.sleep(1)
    print("\nPlease wait for some. The Banking Virtual Environment is loading...")
    time.sleep(1)
    while(True):
        a=int(input("\nPress the required+/ Options...\n1. Depositing Amount \n2. Withdrawing Amount \n3. Checking Balance \n4. Pin Change \n5. Exit\n"))
        os.system('cls')
        if a==1:
              print("\n")
              l = int(input("Enter the Number of Rs.2000 notes : "))
              m = int(input("Enter the Number of Rs.500  notes : "))
              n = int(input("Enter the Number of Rs.200  notes : "))
              o = int(input("Enter the Number of Rs.100  notes : "))
              print("\n")
              notes.update({'2000':l, '500':m, '200':n, '100':o})
              notes1.update({'2000':l, '500':m, '200':n, '100':o})
              time.sleep(1)
              dep=2000*l + 500*m + 200*n + 100*o
              atm_balance += dep
              for key,value in notes1.items():
                  time.sleep(1)
                  print("INR",key," - Notes Deposited : ",value)
              print("\n Thus deposited amount is INR",dep)
              print("\n The Account Balance is INR",dep+account_balance)
        elif a==2:
            w=int(input("\nEnter the Amount to be Withdrawn : \n"))
            if w%100==0 and w<account_balance and w<atm_balance:
                  re=0
                  res=0
                  res1=0
                  res2=0
                  if(w>=2000):
                     re=w//2000
                     res=w%2000
                     print("2000 :",re)
                     update_2000=notes.get('2000')-re
                     notes.update({'2000':update_2000})
                     res1=res//500
                     res=res%500
                     print("500 :",res1)
                     update_500=notes.get('500')-res1
                     notes.update({'500':update_500})
                     res2=res//200
                     res=res%200
                     print("200 :",res2)
                     update_200=notes.get('200')-res2
                     notes.update({'200':update_2000})
                     res3=res//100
                     print("100 :",res3)
                     update_100=notes.get('100')-res3
                     notes.update({'100':update_100})
                     atm_balance-=w
                     account_balance-=w
                  elif(500<=w<2000):
                     re=w//500
                     res=w%500
                     print("500 :",re)
                     update_500=notes.get('500')-re
                     notes.update({'500':update_500})
                     res1=res//200
                     res=res%200
                     print('200 :',res1)
                     update_200=notes.get('200')-res1
                     notes.update({'200':update_200})
                     res2=res//100
                     print('100 :',res2)
                     update_100=notes.get('100')-res2
                     notes.update({'100':update_100})
                     atm_balance-=w
                     account_balance-=w
                  elif(200<=w<500):
                     re=w//200
                     res=w%200
                     print('200 :',re)
                     update_200=notes.get('200')-re
                     notes.update({'200':update_200})
                     res1=res//100
                     print('100 :',res1)
                     update_100=notes.get('100')-res1
                     notes.update({'100':update_100})
                     atm_balance-=w
                     account_balance-=w
                  elif(100<=w<200):
                     res2=w//100
                     print('100 :',res2)
                     update_100=notes.get('100')-res2
                     notes.update({'100':update_100})
                     atm_balance-=w
                     account_balance-=w
                  else:
                     print("enter amount in 100's and 1000's")
            else:
                print("Your account may have insufficient funds or the ATM\nSorry for the convenience")
                          
        elif a==3:
            print("The Current balance is :", account_balance)
        elif a==4:
            p=int(input("Enter Your old pin :\n"))
            if p==1234:
                  p1=int(input("Enter your new pin\n"))
                  p2=int(input("Enter your new pin again\n"))
                  if p1==p2:
                         p=p1
                         return p
                         print("Your new PIN is updated")
                  else:
                      print("Both the passwords don't match")
            else:
                print("Enter the correct Pin")
        elif a==5:
            print("Thank You for using the service")
            break
        time.sleep(2)
        y=int(input("\nPress 1\tTo coninue the process\nPress 2\tExit"))
        if y==1:
            user()
        elif y==2:
            print("Thank You using Union Bank of Switzerland")
            break


print("Welcome to the Union Bank of Switzerland.......")
time.sleep(1.5)
print("\nPlease insert your USB Banking Card....")
time.sleep(1)
for i in range(3):
    a=input("\nEnter your Correct Banking Card Pin....")
    if a.isnumeric():
        print("\nWelcome to the Consumer Banking Portal...")
        user()
        break
    elif a.isalnum():
        print("\nWelcome to the Admin Panel...")
        admin()
        break
    else:
        print("\nThe entered pin is wrong.")
    time.sleep(1.5)
else:
    print("\nYour Card has been blocked, Since You have exceeded maximum log in limit.")
    

        
