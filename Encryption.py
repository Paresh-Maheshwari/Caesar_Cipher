def encrypt(plan_text,key):
    result = ""
    for i in range(len(plan_text)):
        char = plan_text[i]
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)  # ord() functin can convert to string to integer
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)  # chr() functin can convert to integer to string                
    return result

plan_text = str(input("enter a string of plain text :"))
key = int(input("enter a key in integer number : "))

print ("Your Plain Text  is " + plan_text)
print ("Your Key is " + key)
print ("Cipher: " + encrypt(plan_text,key))