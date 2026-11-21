def_string = list(input("Enter your phrase:"))
result = {"Letters": 0, "Digits": 0}
for i in def_string:
    if i.isdigit():
        result["Digits"] += 1
    elif i.isalpha():
        result["Letters"] += 1
print(result)



