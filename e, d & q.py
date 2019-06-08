

done = False

while done == False:
    print("===================")
    print('Type "e" to encrypt')
    print('Type "d" to encrypt')
    print('Type "q" to quit')
    print("===================")
    

    userinput = input("Please enter your choice: ")
    userinput = userinput.lower()
    if userinput == "e":
        message = input("Enter your message to encrypt: ")
        key = int(input("Enter your key: "))
        message1 = ""
        for char in message:
            message1 = message1 + (chr((ord(char)+(key))%126))
        print(message1)
    elif userinput == "d":
        message = input("Enter your message to decrypt: ")
        key = int(input("Enter your key: "))
        message1 = ""
        for char in message:
            message1 = message1 + (chr((ord(char)-(key))%126))
        print(message1)
    elif userinput == "q":
        done = True
