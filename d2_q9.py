a=input("enter the month:")
b=int(input("enter the date :"))
if(b>0):
    if(a=='Mar' or a=='Apr' or a=='May'):
        if(b>20):
            print("it is a summer ")
        else:
           print("it is a winter")
    elif(a=='Jun' or a=='Jul' or a=='Aug'):
        if(b>21):
            print("it is a spring ")
        else:
           print("it is a summar")
    elif(a=='Sep' or a=='Oct' or a=='Nov'):
        if(b>22):
            print("it is a fall ")
        else:
           print("it is a spring")
    elif(a=='Dec' or a=='Jan' or a=='Feb'):
         if(b>21):
             print("it is a winter ")
         else:
             print("it is a fall")
    else:
       print("it is the invalid month")
else:
   print("invaid date")
