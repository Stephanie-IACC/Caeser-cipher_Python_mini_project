alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_cycles = 2
alphabet1 = alphabet * alpha_cycles

def Caeser_Cipher():     
    logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
    
    print("WELCOME TO THE CAESER CIPHER TOOL.")
    print(logo)
    en_co = []
    de_co = []

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        try:
            if direction == "encode":
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n"))
                for eachletter in text:
                    if eachletter in alphabet1:
                        index_eachletter = alphabet1.index(eachletter)
                        E_letter_index = index_eachletter + shift
                        #code=alphabet.index(E_letter_index)
                        encrypted_code1 = alphabet1[E_letter_index]
                        en_co.append(encrypted_code1)
                        encrypted_code = ''.join(en_co)
                print(f"Your message '{text}'" 
                    f" has been encrypted to: {encrypted_code}")
                
                message = input("Do you want to continue with the app? Yes or No:\n").lower().strip()
                print(message)
                try:
                    if message == "yes":
                        continue
                    elif message == "no":
                        print("Goodbye!!!")
                        break
                    else:
                        raise ValueError
                       
                except ValueError:
                    print("Error: Invalid input. Please enter a valid input.")
                    continue

            elif direction == "decode":
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n"))
                for eachletter in text:
                    if eachletter in alphabet1:
                        index_eachletter = alphabet1.index(eachletter)
                        D_letter_index = index_eachletter - shift
                        decoded_code1 = alphabet1[D_letter_index]
                        de_co.append(decoded_code1)
                        decoded_code = ''.join(de_co)
                print(f"Your message '{text}'" 
                    f" has been decoded to: {decoded_code}")
                
                message = input("Do you want to continue with the app? Yes or No:\n").lower().strip()
                print(message)
                try:
                    if message == "yes":
                        continue
                    elif message == "no":
                        print("Goodbye!!!")
                        break
                    else:
                        raise ValueError
                       
                except ValueError:
                    print("Error: Invalid input. Please enter a valid input.")
                    continue

            else:
                raise ValueError 

        except ValueError:
            print("Error: Invalid input. Please enter a valid input.")
            

if __name__ == "__main__":

    Caeser_Cipher()