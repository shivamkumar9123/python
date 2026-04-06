# while True:
#     print("hello")
# count=1
# while count<=5:
#     print("Hello",count)
#     count+=1
    # print(count)

    # i=1
    # while i<=5:
    #     print(i)
    #     i+=1
    # print loop from 1 to 5
# i=5
# while i>=1:
#         print(i)
#         i-=1
# print 1 to 100
# count =1
# while count<=100:
#     print(count)
#     count+=1

    # print 100 to 1
# count =100
# while count>=1:
#   print(count)
#   count-=1

# multiplication 
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#   print(n*i)
#   i+=1
# print square of the number 
# i=1
# while i<=100:
#     print(i*i)
#     i+=1
# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(nums):
#     print(nums[i])
#     i+=1
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=25
# i=0
# while i<len(nums):
#    if(nums[i]==x):
#        print("found",i)
#    i+=1
# break keyword
# i=1
# while i<=10:
#      print(i)
#      if(i==5):
#          break
#      i+=1

   
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found at index",i)
#         break
#     else:
#         print("finding....")
#         i+=1
# print("end of loop")
#  # continue keyword 
# i=0
# while i<=10:
#     if(i==5):
#         i+=1
#         continue
#     print(i)
#     i+=1
# # even through while 
# i=1
# while(i<=100):
#      if(i%2==0):
#         print(i)
#      i+=1
    #  for loop 
# tup=(1,2,3,4,5,6,7,8)
# for num in tup:
#     print(num)
    
# veggies=["potato","onion","cabbage","cauliflower"]
# for val in veggies:
#     print(val)
# else:
#     print("END")
    
# str="sunstone"
# for el in str:
#     if(el=='o'):
#         print(el)
#         break
#     # print(el)
# else:
#     print("END")

# # practice question
# # for me in range(1,11):
# #     print(me*me)
# # me+=1
# idx=0
# nums=[1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)
# for el in nums:
#     if(el==49):
#         print("number founded",idx)
#     idx+=1
# for el in range(1,100,5):
#     print(el)
#     el+=1

# for ys in range(2,51,2):
#     print(ys)
# # multiplication
# n= int(input("enter a number"))
# for i in range(1,11,1):
#     print(n*i)

#  pass 
# for i in range(5):
#     pass
# if(i>5):
#     pass
# print("some useful work")

# sum of first n natural number
i=1
sum=0
while(i<=5):
    sum+=i
    # i+=1
    print("total sum:",sum)
    i+=1
# factorial
fact=1
for el in range(1,10):
    fact*=el
    el+=1
    print("factorial:",fact)
    