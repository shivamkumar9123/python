collection={1,2,4,6,8}
print(collection)
print(type(collection))
collection1={1,2,4,6,8,2,4,"hello world","hello world",9} # set mae duplicate element print nahi hota hai kyuki set immutable hai wo ignore kar deta hai 
print(collection1)   # set unique value and immutable hota hai 
print(len(collection1))                      # set is an unordered that's means any element print anywhere and set is not store in key & keys
collection2={}  # it is not empty set but it is empty dictionary
print(type(collection2))
collection3=set()
print(type(collection3)) # it is empty set
                         # sets is muttable 
                         # sets ->element-> immutable
collection3.add(1)
collection3.add(2)
collection3.add(2)
print(collection3) #add method in sets
collection3.remove(2) # remove method in sets
print(collection3)
collection3.add((4,5,6)) # tuple pass in sets
print(collection3)
#collection3.add([4,8,12]) # list not pass in sets 
#print(collection3)    # hashable means Hash value fixed (constant) ho and  Lifetime me change na ho (immutable ho)
collection4={9,5,3,6,8}
print(collection4)
collection4.clear()
print(len(collection4))
collection5={"hello world","apna college","coding ","python"}
print(collection5.pop())
print(collection5.pop())
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) # unique element {1,2,3,4,5}
print(set1.intersection(set2)) # common element {3}
