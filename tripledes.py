import io
from pyDes import *
import time
secret = input("Enter the Secret Code: ")
imagefile= input("Enter the name of the image file which contains the image to be Encrypted: ")
def time_taken(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return f"{h}:{m}:{round(s,1)}"
    #Encryption

def encryption():
  lst=[]
  with open(imagefile,'rb') as img:
    imgdata = img.read()
    for img1 in imgdata:
        lst.append(img1)
  img.close()

  data = imgdata
  k=triple_des("THISISASECRETKEY",CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode= PAD_PKCS5)
  imgdata=k.encrypt(data)
  with open('Encrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Encryption complete!!!!")

#Decryption

  lst=[]
  with open('Encrypted.jpg','rb') as img:
    imgdata=img.read()
    for img1 in imgdata:
      lst.append(img1)
  img.close()

  data = imgdata
  k =triple_des("THISISASECRETKE1", CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
  imgdata=k.decrypt(data)
  with open('Encrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Decryption complete!!!")

#Encryption

  lst=[]
  with open('Encrypted.jpg','rb') as img:
    imgdata = img.read()
    for img1 in imgdata:
      lst.append(img1)
  img.close()

  data = imgdata
  k=triple_des("THISISASECRETKE2",CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode= PAD_PKCS5)
  imgdata=k.encrypt(data)
  with open('Encrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Encryption complete!!!!")
  print("Encryption ---- Decrytion ----- Encryption complete for Encryption part")

start_time = time.time()
answer_encrypt = encryption()
end_time = time.time()
execution_time = (end_time - start_time)
print(f"Elapsed time: {time_taken(execution_time)}")
def decryption():
  lst=[]
  with open('Encrypted.jpg','rb') as img:
    imgdata=img.read()
    for img1 in imgdata:
      lst.append(img1)
  img.close()

  data = imgdata
  k =triple_des("THISISASECRETKE2", CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
  imgdata=k.decrypt(data)
  with open('Decrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Decryption complete!!!")

#Encryption

  lst=[]
  with open('Decrypted.jpg','rb') as img:
    imgdata = img.read()
    for img1 in imgdata:
      lst.append(img1)
  img.close()

  data = imgdata
  k=triple_des("THISISASECRETKE1",CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode= PAD_PKCS5)
  imgdata=k.encrypt(data)
  with open('Decrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Encryption complete!!!!")

#Decryption

  lst=[]
  with open('Decrypted.jpg','rb') as img:
    imgdata=img.read()
    for img1 in imgdata:
      lst.append(img1)
  img.close()

  data = imgdata
  k =triple_des("THISISASECRETKEY", CBC,"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
  imgdata=k.decrypt(data)
  with open('Decrypted.jpg','wb') as img:
    img.write(imgdata)
  print("Decryption complete!!!")
  print("Decryption ------ Encryption ------- Decryption complete for Decryption part")

decrypt_secret = input("Enter the Secret code :")
if secret == decrypt_secret:
  start_time = time.time()
  final_answer = decryption()
  end_time = time.time()
  execution_time = (end_time - start_time)
  print(f"Elapsed time: {time_taken(execution_time)}")
else:
  print("SECRET CODE INCORRECT --- IMAGE CANNOT BE DECRYPTED")
