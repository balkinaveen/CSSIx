message = input("Enter your message: ")
key = int(input("Enter your key: "))
message1 = ""
for char in message:
    message1 = message1 + (chr((ord(char)-(key))%126))
print(message1)
