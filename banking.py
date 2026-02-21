balance = 0.0

def check_balance():
    if balance>=0:
     print("*************************")
     print(f"checkingg the balaance{balance} ")
     print("*************************")

def depositing(amount):
    global balance
    balance+=amount
    print("*************************")
    print(f" depositing the balance...{balance}")
    print("*************************")
def withdrawl(amount):
    global balance

    if balance>amount:
     balance -= amount
     print("*************************")
     print(f" withdrawling the amount..{amount}")
     print("*************************")
    else:
        print(f"insufficient amount")

def update_kyc(**doc):
    for key,value in doc.items():
        print(f"{key}:{value}")
def check_kyc():
    print(len(dict))




if __name__=="__main__":

    print("*************************")
    print("hey welcome to interest free HALAL BANK ")
    print("*************************")





    while True:


           print("press 1 to check balance")
           print("press 2 to withdraw")
           print("press 3 to deposit")
           print("press 4 to to update kyc")
           print("press 5 to to check kyc")
           print("press 6 to exit")
           print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
           choice=float(input("enter your choice:"))
           print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
           if choice==1:
             check_balance()
           elif choice==2:
            print("*************************")
            bal=float(input("enter your depositing amount:"))
            print("*************************")
            if bal<0:
               print("give correct value!!!")
            else:
               depositing(bal)
           elif choice==3:
            print("*************************")
            w=float(input("enter your withdrawal amount:"))
            print("*************************")
            if w>0:
             withdrawl(w)
            else:
                print("cant withdraw negative amount")



           elif choice==4:

               dict={}


               n=int(input("enter no of document you want to add:"))
               for i in range(n):
                   key=input("enter key for document:")
                   value=input("enter value for document:")
                   dict[key]=value

               update_kyc(**dict)
           elif choice==5:

               check_kyc()
           elif choice == 6:
               break
           else:
             print("*************************")
             print("invalid input!!!")
             print("*************************")
    print("*************************")
    print("thanku 4 banking with us")
    print("*************************")
