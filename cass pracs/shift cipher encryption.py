
def en_shift(char,shift_key):
  if char is ' ':
    return ' '
  if (char.isalpha()):
      off=65
  if(char.islower()):
      off=97
  return chr(off+((ord(char)-off)+shift_key)%26)


def product_encrpyt(message,key):
  temp=''
  for ch in message:
    temp=temp+en_shift(ch,key)
  print(temp) 
  
    

if __name__=='__main__':
  key=int(input("Enter the key: "))
  #key=random.randint(1, 10)    
  de_msg=str(input("enter the message to be encrypted: "))
  print(de_msg)
  print("encrypted message is: ")
  product_encrpyt(de_msg,key)
