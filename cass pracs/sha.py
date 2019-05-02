import hashlib 
import timeit  
# initializing string 
str = input("Enter the string : ")
  
# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest())
print("Length of string is ",len(str))
print(len(result.hexdigest()))
  
print ("\r") 
start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start) 


