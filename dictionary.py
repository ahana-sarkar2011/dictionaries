capitals={"UK":"London","Italy":"Rome"}
print (capitals)
capitals["USA"]="Washington D.C."
print (capitals)
del(capitals["Italy"])
print (capitals)
if "Italy" in capitals:
    print("yes")
else:
    print("no")
x=list(capitals.keys())
print (x)
y=list(capitals.values())
print(y)
print(capitals["UK"])