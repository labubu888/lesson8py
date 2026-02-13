string = str(input("please enter your word: "))

string2 = ('')
for i in string:
    string2 = i + string2

print("\n The orignal word: ",string) 
print("the reversed word: ",string2)  