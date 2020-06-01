num_of_tries = 0
while num_of_tries != 3:
    username = input("Please type your username: ")
    password = input("Please type your password: ")
    if (username == "iaalharbi" and password == "123456"):
        print("Welcome to Gmail")
        exit()
    else:
        print("username or password not correct")
        num_of_tries+=1
        print("You have " +str(3-num_of_tries) + " tries left")