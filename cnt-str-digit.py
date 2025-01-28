word=input("Enter a string:")
s=0
n=0
for i in word:
    if i.isalpha():
        s+=1
    elif i.isdigit():
        n+=1

print("No of string:",s)
print("No of integers:",n)
