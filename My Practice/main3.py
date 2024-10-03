tainput=int(input("Enter number:"))
taiinput2=int(input("Enter another number:"))
oprtr=input("Select an oparator to calculate[+, -, *, /, %]:")
if oprtr=="+":
    result=tainput+taiinput2
    print("You added so addition is", result )
elif oprtr=="-":
    result=tainput-taiinput2
    print("You subtract so subtraction is", result )
elif oprtr=="/":
    result=tainput/taiinput2
    print("You devide so division is", result )
elif oprtr=="%":
    result=tainput%taiinput2
    print("You module so modulas is", result )
elif oprtr=="*":
    result=tainput*taiinput2
    print("You multiply so multiplication is", result )
else:
    print("Please enter an oparator to continue!")

a=2
print(a) 
a=3
print(a)


