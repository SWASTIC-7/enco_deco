import base64
import hashlib
import string
import os
import codecs
import pycipher

def encode():
    
    s = input("Enter the string to encode: ")
    #b_64
    s_bytes = s.encode("utf-8")
    b64_bytes = base64.b64encode(s_bytes)
    b64_string = b64_bytes.decode("utf-8")
    print("Encoded b_64: ", b64_string )

    #b_32
    
    b32_bytes = base64.b32encode(s_bytes)
    b32_string = b32_bytes.decode("utf-8")
    print("Encoded b_32: ", b32_string )
    #md5
    
    s_object = hashlib.md5(s_bytes)
    s_hash = s_object.hexdigest()
    print("Encoded md5: ", s_hash)
    #sha-1
    s_object = hashlib.sha1(s_bytes)
    s_hash = s_object.hexdigest()
    print("Encoded sha-1: ", s_hash)
    #sha-256
    
    s_object = hashlib.sha256(s_bytes)
    s_hash = s_object.hexdigest()
    print("Encoded sha-256: ", s_hash)
    #sha-512
    s_object = hashlib.sha512(s_bytes)
    s_hash = s_object.hexdigest()
    print("Encoded sha-512: ", s_hash)

    #caesar cipher
    for n in range(1, 26):
        ans = ""
        # iterate over the given text
        for i in range(len(s)):
            ch = s[i]
            
            # check if space is there then simply add space
            if ch==" ":
                ans+=" "
            # check if a character is uppercase then encrypt it accordingly 
            elif (ch.isupper()):
                ans += chr((ord(ch) + n-65) % 26 + 65)
            # check if a character is lowercase then encrypt it accordingly
            
            else:
                ans += chr((ord(ch) + n-97) % 26 + 97)
        print("Encoded caesar cipher with shift ", n, " : ", ans)
    
    #rot
    for n in range(1, 26):
         alphabet = string.ascii_lowercase + string.ascii_uppercase
         rot13_alphabet = alphabet[n:] + alphabet[:n]
         translation_table = str.maketrans(alphabet, rot13_alphabet)
         ans = s.translate(translation_table)
         print("Encoded rot with rotation ", n, " : ", ans)
    #rot47
    encoded = ""
    for char in s:
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:  # Check if char is in printable ASCII range
            encoded += chr(33 + ((ascii_val + 14) % 94))
        else:
            encoded += char  # Leave non-printable characters as is
    ans = encoded
    print("Encoded rot47: ", ans)



def decode():
    s = input("Enter the string to decode: ")
    #b_64
    s_bytes = s.encode("ascii")
    b64_bytes = base64.b64decode(s_bytes)
    b64_string = b64_bytes.decode("utf-8")
    print("Decoded b_64: ", b64_string )
    #b_32
    b32_bytes = base64.b32decode(s_bytes)
    b32_string = b32_bytes.decode("utf-8")
    print("Decoded b_32: ", b32_string )
    #md5
    os.system(f"python3 md5_deco.py {s}")
    #caesar_cipher(done the encoder only as cipher rotates)
    for n in range(1, 26):
        ans = ""
        # iterate over the given text
        for i in range(len(s)):
            ch = s[i]
            
            # check if space is there then simply add space
            if ch==" ":
                ans+=" "
            # check if a character is uppercase then encrypt it accordingly 
            elif (ch.isupper()):
                ans += chr((ord(ch) + n-65) % 26 + 65)
            # check if a character is lowercase then encrypt it accordingly
            
            else:
                ans += chr((ord(ch) + n-97) % 26 + 97)
        print("Encoded caesar cipher with shift ", n, " : ", ans)
    #rot13
    ans =  codecs.decode(s,'rot13')
    print('Decoded rot13: ', ans)
    #rot47
    x = ""
    for char in s:
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:
            x += chr(33 + ((ascii_val + 14) % 94))
        else:
            x += char
    print("Decoded rot47: ", x)
    #Atbash
    ans = pycipher.Atbash().decipher(s)
    print("Decoded Atbash: ", ans)
    #baconian
    # lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
	# 		'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
	# 		'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
	# 		'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
	# 		'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
	
    # decipher = ''
    # i = 0

    # s = s.lower()
	  
    # while True:

	#     if(i < len(s)-4):
    #             substr = s[i:i + 5]
    #             if(substr[0] != ' '):
    #                    decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
    #                    i += 5
    #             else:
    #                 decipher += ' '
    #                 i += 1
    #     else:
    #         break
				     
	# print("Decoded baconian: ", decipher)		    
				        
				  
		   

		   
	
		


p = input("Want to encode or decode? (e/d): ")
if p == 'e':
    encode()
elif p == 'd':
    decode()
else:
    print("Invalid input. Please try again.")


