# Python 3 code to demonstrate the 
# working of MD5 (byte - byte) 

import hashlib
import timeit

 
# function
msg = input("Enter your message : ")
result = hashlib.md5(msg.encode()) 
# printing the equivalent byte value. 
print("The byte equiv`alent of hash is : ", end ="") 
print(result.digest())
print("Length of message is ",len(msg))
print("Length of encrypted string is ",len(result.digest()))



start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start) 

