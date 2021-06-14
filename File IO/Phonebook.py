book = []

db = open("db.txt","a")
db.close()

db = open("db.txt","r")
text = db.readlines()
db.close()

for i in range(len(text)):
    text[i]= text[i].strip()
    person = text[i].split(",")
    book.append(person)

while(True):
    mode = input("Do you want to enter, retrieve, or quit:")

    if(mode == "enter"):
        name = input("Enter the name:")
        num = input("Enter the number:")
        person = [name,num]
        book.append(person)
    elif(mode == "retrieve"):
        name = input("Enter the name:")
        for person in book:
            if(person[0]== name):
                print("The number is:"+person[1])
    elif(mode == "quit"):
        db = open("db.txt","w")
        for person in book:
            db.write(person[0]+","+person[1])
        db.close()
        break
