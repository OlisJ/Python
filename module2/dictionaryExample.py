contact_info={
    "alice":{
        "phone":"09128823",
        "email":"random@email.exp",
        "address":"Halit liti",
        "birthday":"01.02.2003"
    },
"blice":{
        "phone":"093131823",
        "email":"main@email.exp",
        "address":"Halil lili",
        "birthday":"03.02.2003"
    },
"clice":{
        "phone":"113131823",
        "email":"sec@email.exp",
        "address":"ramadan dani",
        "birthday":"03.03.2003"
    }
}

#print blice info
#create 2 new personas
#print jane info
#update jane phonenumber and print

print(contact_info["blice"])
contact_info["jane"]={"phone":"123321","email":"email@email.com","addess":"dikun","birthday":"02.09.08"}
contact_info["john"]={"phone":"125521","email":"email@hotmail.com","addess":"qaty","birthday":"11.11.08"}
print(contact_info)
contact_info["jane"]['phone']="112233"
print(contact_info['jane']["phone"])
