errors={"200":"success","301":"permanent redirect","302":"temporary redirect","304":"not modified","400":"bad request","404":"not found"}
number=input("number:")
if number in errors:
    print(errors[number])
else:
    print("error code does not exist")