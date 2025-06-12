lines=["Hello World!\n","Welcome to Python\n"]
with open("example.txt","w") as file: #we open the file w permission to write
    file.writelines(lines) #we write on multiple lines