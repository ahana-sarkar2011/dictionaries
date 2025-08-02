vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
word=input("What is your word?")
word=word.lower()
for i in word:
    if i in vowels:
        vowels[i]+=1
        
print(vowels)