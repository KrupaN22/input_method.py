bank=int(input("enter your amount:"))
while True:
    
    if bank>0:
     print("account is open")
     print("="*20)
    
     print("enter1(for deposite)")
     print("enter2(for withdraw)")
     print("enter3(press 3 for balance)")
     print("enter4(press 4 for exit)")
    choice=int(input("enter your choice :"))

    if choice==1:
        a=int(input("enter a amount for deposite:"))
        bank +=a 
        print(f"this is new amount{bank}")
   
    elif choice==2:
        b=int(input("enter a amount for withdraw:"))
        bank -=b
        print(f"this is new {bank}")

    elif choice==3:
        print(f"my current amount is {bank}")
        break

    elif choice==4:
        print(f"khatam tata bye bye")
    else:

        print("invalid number")

else:
   print("account is close")
    
    



