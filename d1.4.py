try:
    num=int(input("enter any number"))
    x=num
    rev=0
    while num>0:
        r=num%10
        rev=(rev*10)+r
        num=num//10
    if x==rev:
        print("the given number is palindrome")
    else:
          print("the given number is not a palindrome")
except ValueError:
    print("its not a valid input")
