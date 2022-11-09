def decrypt(key, cipher_Text):
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in cipher_Text:
        if (letter.isupper()):
            if letter in u_alpha:
                letter_index = (u_alpha.find(letter) - key) % len(u_alpha)
                result = result + u_alpha[letter_index]
            else:
                result = result + letter         
        else:
            if letter in l_alpha:
                letter_index = (l_alpha.find(letter) - key) % len(l_alpha)
                result = result + l_alpha[letter_index]
            else:
                result = result + letter

    return result


cipher_Text = input("Enter the cipher text : ")

key = int(input("Enter the key integer number : "))
print("Cipher  text  : " + cipher_Text)

print ("Cipher: " + decrypt(key,cipher_Text))
