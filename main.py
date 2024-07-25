import os
import pwinput

# from bullet import Password

def showmenu():
  a="State Bank of House 32"
  print("\n",a. center(70))
  print("*****MENU*****")
  print("\n1.Check Balance")
  print("2.Deposit Amount")
  print("3.Withdraw Amount")
  print("4.Exit\n")
  print("****************")



balance=1000
option=0
for i in range(0,3):
  try:
    password = int(pwinput.pwinput(prompt ="Enter your PIN for accesing your bank account: ", mask="*"))
    os.system('clear')
    
    if(password==1022):
      # print("\nYour password is:", password)
    
      while(option!=4):
        showmenu()
        option =int(input("\nEnter the option:"))
        os.system('clear')
        match option:
          
           case 1: 
             print("Balance is:", balance,"$\n")
          
           case 2 :
             deposit=  int(input("\nEnter Deposit Amount:"))  
             balance=balance+deposit
             print("\nYour Amount is Successfully Deposited to your account.")
             # print(f"\nBalance is: {balance} $")
        
           case 3: 
             withdraw=int(input("Enter Withdraw Amount:"))
             if(balance>=withdraw):
               balance=balance-withdraw
               print("\nYour Amount is Successfully Withdraw from your account.")
               # print(f"\nBalance is: {balance} $")
             else:
               print("\nNot Enough Money")  
           case 4: print("\nGood Bye Sir/Madam and Have a Good Day.")
    else:
      print("\nPIN is Incorrect")
  except:
    print("\n Invalid Input , PIN must be in Digits")
  