string_= input("Enter a word : ")
new=""
for i in string_:
    if i.isalpha():
        asc = ord(i)
        if 65 <= asc <= 90:new = new + chr((asc + 32))
        else:new = new + chr((asc - 32))
    else:
        new=new+str(i)
print(new)