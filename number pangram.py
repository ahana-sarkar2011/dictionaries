numbers={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
phrase=input("Please state your number")
for i in phrase:
    if i in numbers:
        numbers[i]+=1
if 0 in numbers.values():
    print("That number is not a pangram")
else:
    print("That number is a pangram")