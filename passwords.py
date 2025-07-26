passwords={"Ahana":"qwerty10","Mahi":"uiop14","Lily":"asdf123","Olivia":"GHJkl15"}
user=input("USERNAME:")
if user in passwords:
    pw=input("PASSWORD:")
    if pw == passwords[user]:
        print("You have logged in")
    else:
        print("wrong password")
else:
    print("username does not exist")