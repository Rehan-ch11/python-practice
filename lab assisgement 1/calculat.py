def calculator():
    while True:
        print("calculator;")
        print("ENTER 1 for addition;")
        print("ENTER 2 for subtraction;")
        print("ENTER 3 for multiply;")
        print("ENTER 4 for division;")
        print("ENTER 5 for exit;")

        choice=int(input("ENTER your choice:"))
        if choice in ( 1,2,3,4):
            num1=int(input("ENTER 1st number"))
            num2=int(input("ENTER 2nd number"))

        if (choice==1):    
            print("your additicon is :",num1+num2)
        if (choice==2):
            print("your subtraction is :",num1-num2)
        if(choice==3):
            print('your multiplication is :',num1*num2)
        if(choice==4):             
             print("your division is :",num1/num2)
        if(choice==5):
            print("exit")
            break
            


calculator()