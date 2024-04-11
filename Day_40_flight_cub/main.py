import sheety


print("Welcome to My_flight Club\nWe Find the best Flight deals and email you.")
user_first_name = input("What is your name?\n")
user_last_name = input("What is your last name?\n")

in_club = False
email_check = True
while email_check:
    user_email = input("What is your email?\n")
    user_email_2 = input("Type your email again\n")

    if user_email != user_email_2:
        print("\n\nYour Email is not correct Try again!!")
    
    elif user_email.lower() == 'quit':
        exit()
    else:
        email_check = False


sheety.post_new_row(user_first_name,user_last_name,user_email)