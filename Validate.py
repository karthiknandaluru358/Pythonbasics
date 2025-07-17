#validate user input exercise
#1.username is no more than 12 characters
#2 username must not contain spaces
#3 username must not contain digits.

username=input("Enter the valid username: ")
length=len(username)
result=username.find(" ")
result2=username.isalpha()

if length<=12 and result -1 and result2:
    print("It's a valid username")
else:
    print("Its not a valid username please enter the valid username")