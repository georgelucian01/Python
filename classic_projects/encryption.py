from generate_encryption_keys import encryption

def main(): 
    
    # ask if you want to generate new keys
    while True:
        q1 = input("Do you want to generate new keys? (yes/no): ").lower()
        if q1 == "yes":
            encryption.generate_keys("classic_projects/encryption_data.json")
            break
        elif q1 == "no":
            break
        else:
            continue
        
    chars, keys = encryption.read_from_json("classic_projects/encryption_data.json")

    # ask for encrypt of decrypt
    while True:
        q2 = input("Do you to encrypt or decrypt? (enc\dec): ").lower()
        if q2 == "enc":

            plain_text = input("Enter message to encrypt: ")
            encrypted = encryption.encrypt_decrypt(plain_text, chars, keys)
            print()
            print(f"Encrypted text is: {encrypted}")
            print()

        elif q2 == "dec":

            plain_text = input("Enter message to decrypt: ")
            decrypted = encryption.encrypt_decrypt(plain_text, keys, chars)
            print()
            print(f"Decrypted text is: {decrypted}")
            print()
        else:
            continue
        break
                    
       
    
   

if __name__ == "__main__":
    main()