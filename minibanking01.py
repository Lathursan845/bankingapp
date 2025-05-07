def creat_auto_user_id():

        try:
                with open('customers.txt',"r")as file:
                        lines = file.readlines()
                        if not lines:
                                return 1000
                        last_id = int(lines[-1].split(',')[0])
                        return last_id +1             
        except FileNotFoundError :
                return 1000
        


def get_customer_info():
        user_id = creat_auto_user_id()
        name=input("Enter the name :")
        address=input("Enter the address :")
        username=input("Enter the user name :")
        password=input("Enter the password :")
        
        customer_data = (f"{name},{address}\n")
        user_credentials = (f"{user_id},{username},{password}\n")
        

        with open('customers.txt',"a")as file:
                file.write(customer_data)

        with open('users.txt',"a")as file:
                file.write(user_credentials)

get_customer_info()

def create_account():

        try:
                with open ("Acc.No","r")as file:
                        lines=file.readlines()
                        if not lines:
                                return 2000
                        last_id = int(lines[-1].split(',')[0])
                        return last_id +1             
        except FileNotFoundError :
                return 2000
        
def creat_account():
        Account_number=input("Enter the  Account_number:")
        Name=input("Enter the holder name:")
       # password=input("Enter the password:")
        Acc_data = (f"{Account_number},{ Name}\n")
        print(Acc_data)
        print("Succesfully Created !.")
        with open('Acc.txt',"a")as file:
                file.write(Acc_data)
creat_account()
        

            
# name=input("Enter your name:")
# balance=float(input("Enter initial balance:"))
# if balance < 0:
#             print("balance must be zero or more.")
#             return

# account_number=str(len(accounts)+1)
# accounts[account_number]={"name":name,
#                           "balance":balance,
#                           "transactions":[f"Account created with balance{balance}"]}
# print("account created." "Your account number is",{account_number})




# def login():
#     print('Welcome to banking app')
#     username=input("enter your name:")
#     password=input("Enter your password:")
#     if username in users and users[username]["password"]==password:
#         print(f"welcome,{username}")
#     else:
#         print("invaild details try again.")


# def deposit():
#     acc=input("enter account number:")
#     if acc not in accounts:
#         print("Account not found.")
#         return
#     accounts[acc]["balance"]+=amount_account[acc]







