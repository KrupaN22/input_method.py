total = int(input("enter a amount:"))
while True:
    if total>0:
         print("="*20)

    print("enter1(for add item)")
    print("enter2(for show total bill)")
    print("enter3(for Exit)")

    choice = int(input("enter your choice:"))

    if choice==1:
         price = int(input("enter item price"))
         total-= price
         print(f"Item is added succesfully")

    elif choice==2:
            print("your total bill is:",{total})
      
    elif choice==3:
          print("Thank you for shopping!")
          break
    else:
          print("invalid price")
   

        

            


     
    
       
