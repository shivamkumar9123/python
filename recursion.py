# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
# # function
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal_sum(5,10)
# cal_sum(20,30)
# cal_sum(100,200)
# def print_hello():
#     print("hello")
# output=print_hello()
# print(output)  # None is a special value in Python that represents the absence of a value or a null value. It is often used to indicate that a function does not return anything or to signify that a variable has no value assigned to it. When a function does not explicitly return a value, it implicitly returns None.
# def three_sum(a,b,c):
#     sum=a+b+c
#     print(sum)
#     return sum
# three_sum(12,15,22)
# # average of three numbers
# def three_sum(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(sum)
#     print("avg:",avg)
    
#     return sum,avg
# three_sum(12,15,22)
# print(" i am learning python",end=" & ") # sep=" " is used to separate the values with a space, and end="\n" is used to add a newline character at the end of the output. By default, print() adds a newline character at the end of the output, so if you want to change that behavior, you can use the end parameter.
# print("i am present in class")   # end=" " is used to keep the output on the same line, and sep=" " is used to separate the values with a space. By default, print() adds a newline character at the end of the output, so if you want to change that behavior, you can use the end parameter.

# def calc_prod(a,b=10):
# #def calc_prod(a=10,b):# SyntaxError: non-default argument follows default argument
#     prod=a*b
#     print(prod)
#     return prod
#     #calc_prod() # TypeError: calc_prod() missing 2 required positional arguments: 'a' and 'b'
# calc_prod(5) # 50
# #


# cities=["delhi","mumbai","kolkata","chennai"]
# heroes=["superman","batman","spiderman","ironman"]
# def print_cities(list):
#     print(len(list))
# print(len(cities))
# print(len(heroes))
# #print a list in single line
# heroes=["superman","batman","spiderman","ironman"]
# print(heroes[0],end=" ")
# print(heroes[1],end=" ")
# #
cities=["delhi","mumbai","kolkata","chennai"]
def print_cities(list):
    for item in list:
        print(item,end=" ")
    print()
print_cities(cities)

# factorial of a number using recursion
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
print(factorial)
factorial(5)
factorial(10)
factorial(9)

# converter 
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
converter(1)
converter(2)
# temperature converter
def temp_converter(celsius):
    fahrenheit=(celsius*9/5)+32
    print(celsius,"C=",fahrenheit,"F")
temp_converter(0)
temp_converter(100) 
# user input 
num=int(input("enter a number:"))
def function(num):
    if(num%2==0):
        print("Even:",num)
    else:
        print("Odd:",num)
function(num)

def fun(num):
    if(num==0):
        return 
    print(num)
    fun(num-1)
fun(5)
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(9))
#first n natural number sum using recursion
num=int(input("enter a number:"))
def sum_natural(num):
    if(num==1):
        return 1
    return sum_natural(num-1)+num
print(sum_natural(num))

def fruits(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    fruits(list,idx+1)
fruits=["apple","banana","grapes","orange"]
print(fruits)