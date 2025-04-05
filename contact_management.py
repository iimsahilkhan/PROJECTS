print("    CONTACTS    ")
print("----------------")
print("(+) to create contact \n (-) to delete contact \n (search) to search \n "
    "(all) to list all \n (e) to exit \n ")
contacts={}

def add_contact(name,ph_num,email):
    contacts[name]={"phone number":ph_num,"email":email}

def del_contact(name):
    del(contacts[name])

def search_contact(name):
    return contacts[name]

def list_all():
    return contacts.items()


choice=""
while(choice!="exit"):
    choice=input("enter your choice : ")
    if(choice=="+"):
        name=input("enter name : ")
        if name in contacts:
            print(f"contact already exists")
        else:
            ph_num=eval(input("enter ph number : "))
            email=input("enter email :")
            add_contact(name,ph_num,email)
            print("contact added succesfully \n ")
    elif(choice=="-"):
        name=input("enter name: ")
        if name in contacts:
            del_contact(name)
            print("contact deleted successfully \n ")
        else:
            print(f"no contact found to delete")
    elif(choice=="search"):
        name=input("enter name : ")
        if name in contacts:
            print(f" contact details of {name} :{search_contact(name)}\n")
        else:
            print(f"contact not found")
    elif(choice=="all"):
        print(f"all contacts list : \n {list_all()}\n")