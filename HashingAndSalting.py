#MODULE USED - HASHLIB
import hashlib
encrypted_text = "messageIsVeryLargeOrVeryVeryLArge"
#Salting Algorithm
def salt(text):
    temp = ""
    j = 0
    salt = "ezioishan"
    for i in range(len(text)):
        if(i%2):
            temp += text[i]
        else:
            temp += salt[j%len(salt)]
            j += 1
    return temp

#SENDER'S END:
encrypted_salted_text = salt(encrypted_text)
#hashing done through SHA-256 algorithm
Sender_HASH = hashlib.sha256(encrypted_salted_text.encode()).hexdigest()


#RECEIVER'S END:
received_text = encrypted_text
received_salted_text = salt(received_text)

Receiver_HASH = hashlib.sha256(received_salted_text.encode()).hexdigest()

#AUTHENTICATION:
if(Sender_HASH == Receiver_HASH):
    print("Sender Authenticated! Message sent is genuine.")
else:
    print("Authentication Failed!")
