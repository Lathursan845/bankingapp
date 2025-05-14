# from datetime import datetime
# Date_Time_Now = datetime.now()
# def creat_auto_user_id():
       


#         try:
#                 with open('users.txt',"r")as file:
#                         lines = file.readlines()
#                         if not lines:
#                                 return 1000
#                         last_id = int(lines[-1].split(',')[0])
#                         return last_id +1             
#         except FileNotFoundError :
#                 return 1000
# # def get_customer_info():
# #         user_id = creat_auto_user_id()
# #         name=input("Enter the name :")
# #         address=input("Enter the address :")
# #         username=input("Enter the user name :")
# #         password=input("Enter the password :")
        
# #         customer_data = (f"{name},{address}\n")
# #         user_credentials = (f"{user_id},{username},{password}\n")
        

# #         with open('customers.txt',"a")as file:
# #                 file.write(customer_data)

# #         with open('users.txt',"a")as file:
# #                 file.write(user_credentials)





# accounts = {}

# def create_account():
    
#         #def get_customer_info():
#         user_id = creat_auto_user_id()
#         name=input("Enter the full name:")
#         address=input("Enter the address :")
#         username=input("Enter the user name :")
#         password=input("Enter the password :")

#         customer_data = (f"{name},{address}\n")
#         user_credentials = (f"{user_id},{username},{password}\n")

#         try:
#                 with open('customers.txt',"a")as file:
#                         file.write(f'{customer_data}')

#                 with open('users.txt',"a")as file:
#                         file.write(user_credentials)

        

#                 #account_number =str(uuid.uuid4())[:4] 
#         #account_number =int(input("Enter account num:"))




#                 account_number=input("enter the account number:")
#                 #name = input("Enter account holder's name: ")
        
#                 initial_balance = float(input("Enter initial deposit (>= 0): "))
#                 if initial_balance > 0:
#                         with open('balance.txt','a')as file:
#                                 file.write(f'{account_number},{name},{initial_balance}\n')
#                                 accounts[account_number] = {
#                         "name": name,
#                         "balance": initial_balance,
#                         "transactions": [("Initial Deposit", initial_balance)]
#                                                                 }
#                         print(f"Account created successfully. Account Number: {account_number}")
#                         return accounts


#                 print("Initial balance must be non-negative.")
#                 return
#         except ValueError:
#                 print("Invalid input. Please enter a number.")

#         accounts[account_number] = {
#         "name": name,
#         "balance": initial_balance,
#         "transactions": [("Initial Deposit", initial_balance)]
#     }
#         print(f"Account created successfully. Account Number: {accounts}")
   

# def deposit_money():
#         global Date_Time_Now
#         try:
#                 statement = 'deposit'   
#                 account_number = input("Enter account number: ")
#                 with open("balance.txt",'r') as file:
#                       bal1 = file.readlines()
#                 for bal2 in bal1:
#                       bal3 = bal2.strip().split(',')
#                 if account_number == bal3[0]:
#                         balance = float(bal3[2])
        
#                         amount = float(input("Enter deposit amount: "))
#                         if amount > 0:
#                                 balance += amount
#                                 print("Deposit successful.")
#                         else:
#                                 print("Deposit must be a positive number.")
                        
#                         with open('Deposit.txt','a')as file:
#                                 file.write(f'{ account_number},{ amount}{ statement}\n')
#                 else:
#                       print("Account Number not found!")
                        
#         except ValueError:
#                 print("Invalid input.")
#                 return

    



# # def withdraw_money():
# #     global Date_Time_Now
# #      try:
# #         statement = 'withdraw'
# #         account_number = input("Enter account number: ")
# #         with open("Deposit.txt",'r') as file:
# #                         bal1 = file.readlines()
# #         for bal2 in bal1:
# #                         bal3 = bal2.strip().split(',')
# #         if account_number == bal3[0]:
# #                                 Deposit = float(bal3[2])
                
# #         #if account_number not in accounts:
# #         #print("Account not found.")

# #                                 amount = float(input("Enter withdrawal amount: "))
# #                                 if amount <= 0:
# #                                 print("Amount must be positive.")
                
# #                                 if amount > accounts[account_number]["balance"]:
# #                                 with open('Deposit.txt','a')as file:
# #                                         file.write(f'{ account_number  },{ amount},{statement}\n')
# #                                 print("Insufficient balance.")
        
# #         except ValueError:
# #         print("Invalid input.")
# #         return

# #     accounts[account_number]["balance"] -= amount
# #     accounts[account_number]["transactions"].append(("Withdrawal", amount))
# #     print("Withdrawal successful.")

# #---------------------------------------------------------------------------------------------------------------------------------------------------
# def withdraw_money():
#     global Date_Time_Now
     
#     try:
#         statement = 'withdraw'
#         account_number = input("Enter account number: ")

        
#         with open("Deposit.txt", 'r') as file:
#             bal1 = file.readlines()

       
#         account_found = False
#         for bal2 in bal1:
#             bal3 = bal2.strip().split(',')
#             if account_number == bal3[0]:
#                 account_found = True
#                 Deposit = float(bal3[2])  
#                 amount = float(input("Enter withdrawal amount: "))
#                 if amount <= 0:
#                     print("Amount must be positive.")
#                     return
                
#                 if amount > Deposit:
#                     print("Insufficient balance.")
#                     return
                
               
#                 Deposit -= amount  

               
#                 with open("Deposit.txt", 'w') as file:
#                     for line in bal1:
#                         bal3 = line.strip().split(',')
#                         if bal3[0] == account_number:
#                             file.write(f"{bal3[0]},{bal3[1]},{Deposit}\n")
#                         else:
#                             file.write(line)
                
               
#                 print(f"Withdrawal of {amount} successful. New balance: {Deposit}")
#                 with open('Deposit.txt','a')as file:
#                                 file.write(f'{ account_number},{ amount}{ statement}\n')
#             else:
        
#                 if not account_found:
#                         print("Account number not found.")
            
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")


# def check_balance():
#     account_number = input("Enter account number: ")
#     with open("users.txt","r")as file:
#         for line in file:
#                 data = line.strip().split(",")
#                 if len(data) == 3: 
                        
#                         account, name, balance = data
#                 accounts[account] = {"name": name, "balance": float(balance)}
    
#                 print("Account not found.")
#                 return
#         balance = accounts[account_number]["balance"]
#         print(f"Current balance: ${balance:.2f}")



# def view_transaction_history():
#     account_number = input("Enter account number: ")
#     if account_number not in accounts:
#         with open('transaction.txt','a')as file:
#                 file.write(f'{ account_number  }\n')
#         print("Account not found.")
#         return
#     for transaction in accounts[account_number]["transactions"]:
#         print(f"{transaction[0]}: ${transaction[1]:.2f}")


# def main_menu():
#     while True:
#         print("\n--- Mini Banking App ---")
#         print("1. Create Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Check Balance")
#         print("5. View Transaction History")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             create_account()
#         elif choice == "2":
#             deposit_money()
#         elif choice == "3":
#             withdraw_money()
#         elif choice == "4":
#             check_balance()
#         elif choice == "5":
#             view_transaction_history()
#         elif choice == "6":
#             print("Thank you for using the banking app!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

#         #if __name__ == "_main_":

#main_menu()
        




#         try:
#                 with open ("Acc.No","r")as file:
#                         lines=file.readlines()
#                         if not lines:
#                                 return 2000
#                         last_id = int(lines[-1].split(',')[0])
#                         return last_id +1             
#         except FileNotFoundError :
#                 return 2000
        
# def creat_account():
#         Account_number=input("Enter the  Account_number:")
#         Name=input("Enter the holder name:")
#        # password=input("Enter the password:")
#         Acc_data = (f"{Account_number},{ Name}\n")
#         print(Acc_data)
#         print("Succesfully Created !.")
#         with open('Acc.txt',"a")as file:
#                 file.write(Acc_data)
# creat_account()
        

            
# # name=input("Enter your name:")
# # balance=float(input("Enter initial balance:"))
# # if balance < 0:
# #             print("balance must be zero or more.")
# #             return

# # account_number=str(len(accounts)+1)
# # accounts[account_number]={"name":name,
# #                           "balance":balance,
# #                           "transactions":[f"Account created with balance{balance}"]}
# # print("account created." "Your account number is",{account_number})




# # def login():
# #     print('Welcome to banking app')
# #     username=input("enter your name:")
# #     password=input("Enter your password:")
# #     if username in users and users[username]["password"]==password:
# #         print(f"welcome,{username}")
# #     else:
# #         print("invaild details try again.")


# # def deposit():
# #     acc=input("enter account number:")
# #     if acc not in accounts:
# #         print("Account not found.")
# #         return
# #     accounts[acc]["balance"]+=amount_account[acc]

#===================================================================================================
from datetime import datetime
Date_Time_Now = datetime.now()
def creat_auto_user_id():
       


        try:
                with open('users.txt',"r")as file:
                        lines = file.readlines()
                        if not lines:
                                return 1000
                        last_id = int(lines[-1].split(',')[0])
                        return last_id +1             
        except FileNotFoundError :
                 return 1000
def main_menu():
    while True:
        print("\n--- Welcome to  Banking App ---")
        # print("1.Admin")
        # print("2.User")
        # choice =input("choice an option")
        # if choice == "1":
        #       user name
            

        # choice=("enter the choice")
        # if choice =="1":
        print("1. Create_Account")
        print("2. Deposit_Money")
        print("3. Withdraw_Money")
        print("4. Check_Balance")
        print("5. View_Transaction_History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            creat_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_transaction_history()
        elif choice == "6":
            print("Thank you for using the banking app!")
            break
        else:
            print("Invalid choice. Please try again.")


#=========================================================================================================
accounts = {}

def creat_account():
        user_id=creat_auto_user_id()
         #account_number=input("enter the account account_number")
        global Date_Time_Now
        name=input("enter the full_name:")
        address=input("enter the address:")
        user_name=input("enter the name:")
        password=input("enter the password:")
        phone_number=input("enter the phone number:")

        customer_data = (f"{name},{address},{phone_number}\n")
        user_credentials = (f"{user_id},{user_name},{password}\n")

        try:
                with open('customers.txt',"a")as file:
                        file.write(f'{customer_data}')

                with open('users.txt',"a")as file:
                        file.write(user_credentials)

                account_number=input("enter the account number :")
                initial_balance = float(input("Enter initial balance (>0): "))
                if initial_balance > 0:
                        with open('balance.txt','a')as file:
                                file.write(f'{account_number},{name},{initial_balance}\n')
                                accounts[account_number] = {
                        "name": name,
                        "balance": initial_balance,
                        "transactions": [("Initial Deposit", initial_balance)]
                                                                }
                        print(f"Account created successfully. Account Number: {account_number}")
                        return accounts


                print("Initial balance must be non-negative.")
                return
        except ValueError:
                print("Invalid input. Please enter a number.")

        accounts[account_number] = {
        "name": name,
        "balance": initial_balance,
        "transactions": [("Initial Deposit", initial_balance)]
    }
        print(f"Account created successfully. Account Number: {accounts}")

#===================================================================================================================
def deposit_money():
        global Date_Time_Now
        try:
                statement = 'deposit'   
                account_number = input("Enter account number: ")
                with open("balance.txt",'r') as file:
                      bal1 = file.readlines()
                for bal2 in bal1:
                      bal3 = bal2.strip().split(',')
                if account_number == bal3[0]:
                        balance = float(bal3[2])
        
                        amount = float(input("Enter deposit amount: "))
                        if amount > 0:
                                balance += amount
                                print("Deposit successful.")
                        else:
                                print("Deposit must be a positive number.")
                        
                        with open('Deposit.txt','a')as file:
                                file.write(f'{ account_number},{ amount}{ statement}\n')
                else:
                      print("Account Number not found!")
                        
        except ValueError:
                print("Invalid input.")
                #return

def withdraw_money():
    global Date_Time_Now
     
    try:
        statement = 'withdraw'
        account_number = input("Enter account number: ")

        
        with open("Deposit.txt", 'r') as file:
            bal1 = file.readlines()

       
        account_found = False
        for bal2 in bal1:
            bal3 = bal2.strip().split(',')
            if account_number == bal3[0]:
                account_found = True
                Deposit = float(bal3[2])  
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    return
                
                if amount > Deposit:
                    print("Insufficient balance.")
                    return
                
               
                Deposit -= amount  

               
                with open("Deposit.txt", 'w') as file:
                    for line in bal1:
                        bal3 = line.strip().split(',')
                        if bal3[0] == account_number:
                            file.write(f"{bal3[0]},{bal3[1]},{Deposit}\n")
                        else:
                            file.write(line)
                
               
                print(f"Withdrawal of {amount} successful. New balance: {Deposit}")
                with open('Deposit.txt','a')as file:
                                file.write(f'{ account_number},{ amount}{ statement}\n')
            else:
        
                if not account_found:
                        print("Account number not found.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def check_balance():
    account_number = input("Enter account number: ")
    with open("users.txt","r")as file:
        for line in file:
                data = line.strip().split(",")
                if len(data) == 3: 
                        
                        account, name, balance = data
                accounts[account] = {"name": name, "balance": float(balance)}
    
                print("Account not found.")
                return
        balance = accounts[account_number]["balance"]
        print(f"Current balance: ${balance:.2f}")

def view_transaction_history():
        account_number = input("Enter account number: ")
        if account_number not in accounts:
                with open('transaction.txt','a')as file:
                        file.write(f'{ account_number  }\n')
        print("Account not found.")
        #return
        for transaction in accounts[account_number]["transactions"]:
                print(f"{transaction[0]}: ${transaction[1]:.2f}")

main_menu()
# def main_menu():
#     while True:
#         print("\n--- Mini Banking App ---")
#         print("1. Create_Account")
#         print("2. Deposit_Money")
#         print("3. Withdraw Money")
#         print("4. Check Balance")
#         print("5. View Transaction History")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             create_account()
#         elif choice == "2":
#             deposit_money()
#         elif choice == "3":
#             withdraw_money()
#         elif choice == "4":
#             check_balance()
#         elif choice == "5":
#             view_transaction_history()
#         elif choice == "6":
#             print("Thank you for using the banking app!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

#         #if __name__ == "_main_":


        


    



         




