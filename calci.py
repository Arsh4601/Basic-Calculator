choice="yes"
print("Enter 1 to add")
print("Enter 2 to subtract")
print("Enter 3 to multiply")
print("Enter 4 to divide")


while True:
    ans=int(input("Your choice?: "))
    num1=input("\nEnter 1st number: ")

    try:
        num1=int(num1)
    except:
        try:
            num1=float(num1)
        except:
            print("Invalid Entery")

    num2=input("\nEnter 2nd number: ")
    try:
        num2=int(num2)
    except:
        try:
            num2=float(num2)
        except:
            print("Invalid Entery")

    if(ans==1):
        print(num1+num2)
    elif(ans==2):
        print(num1-num2)
    elif(ans==3):
        print(round((num1*num2),2))
    elif(ans==4):
        print(round((num1/num2),2))
    else:
      print("Invalid choice\n")
      
    choice=input("Do you wish to continue(y/n): ")

    if(choice=="no" or choice=="n"):

        break

    
