from Crypto.Cipher import AES
import os.path
from termcolor import colored



BS = 16
def pad(s):
    s += chr(BS - len(s)%BS)*(BS - len(s)%BS)
    return s

os.system('clear')
print colored("enter your choice :", 'red')
print colored("1:Encrypt", 'cyan')
print colored("2:Decrypt",'yellow')
choice = raw_input(colored("enter choice: " ,'red'))


if choice == '1':

	print colored("create a text file with name message and store your data",'green')	
	exists =os.path.isfile("message.txt")
	if exists:
		print colored("file found",'red')
		key = raw_input(colored("enter your password/key(16 charecter) = " ,'green'))
		Enc_Type = AES.new(key,AES.MODE_ECB)
		message = open("message.txt").read()
		pad_msg = pad(message)
		#DO Encryption
		cipher = Enc_Type.encrypt(pad_msg)
		open("encoded" + ".enc" ,'w').write(cipher)
		os.remove("message.txt")
		print colored("encption done, original file deleted ,generated encrypted file Encoded.enc" , 'green')
		print colored("exiting....",'red')
		quit()
	else:
		print colored("file not found ..",'red')
		print colored("message.txt created paste you data there",'red')
		dummy = "dummy text"
		open("message.txt",'w').write(dummy)
		quit()	
	

elif choice == '2':

	print colored("store encoded.enc in same folder",'green')
	exists = os.path.isfile("encoded.enc")
	if exists:
		print colored("encoded file found",'green')
		key = raw_input(colored("enter your password/key to decrypt(16 charecter) = ",'green'))
		Dec_Type = AES.new(key,AES.MODE_ECB)
		#DO decrypt
		file = open("encoded.enc").read()
		decipher = Dec_Type.decrypt(file)
		open("decrypted.txt",'w').write(decipher)
		print colored("decryption done . decrypted.txt created",'green')
		print colored("exiting .... ",'red')
		quit()
	else:
		print colored("store encoded.enc to the same folder and try again",'green')
		quit()


else:
	print colored("wrong input exiting.....",'red')
	quit()
