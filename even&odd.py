# num=int(input("enter the number:"))
# if(num %2==0):
#     print("even")
# else:
#     print("odd")
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if(a>=b and a>=c):
#     print("first number is largest",a)
# elif(b>=c):
#     print("second number is largest",b)
# else:
#     print("third number is largest",c)
# num=int(input("enter the number:"))
# if(num%7==0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
d=int(input("enter the fourth largest number:"))
if(a>=b and a>=c and a>=d):
    print("first number is largest",a)
elif(b>=c and b>=d):
    print("second number is largest:",b)
elif(c>=d):
    print("third number is largest ",c)
else:
    print("fourth number is largest",d)

