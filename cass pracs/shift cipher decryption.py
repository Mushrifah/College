
def de_shift(char,shift_key):

  if char is ' ':
    return ' '
  if (char.isalpha()):
      off=65
  if(char.islower()):
      off=97  

  return chr(off+((ord(char)-off)-shift_key)%26)

def product_decrpyt(message,key):
  temp=''
  for ch in message:
    temp=temp+de_shift(ch,key)
  print(temp) 


if __name__=='__main__':
  key=int(input("Enter the key: "))
  en_msg=str(input("enter the encrypted message: "))
  print(en_msg)
  print("the decrypted message is: ")
  product_decrpyt(en_msg,key)