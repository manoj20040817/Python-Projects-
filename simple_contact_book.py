"A Simple Contact Book using dict, str, list, bool data types and functions"


contacts = {
  
  "manoj": "96359489890",    
  "rahul": "76784922664",
  "mahesh": "8922376666",
  "dilli": "78647889378"
  
}
 
def add_contact(name, phone):
    contacts[name] = phone #contacts[key] = value

def search_contact(name):
    if name in contacts:
        print(f"{name}:{contacts[name]}")
    else:
        print("contact not found")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted")
    else:
        print("contact not found")
# def show_contacts():
#     for name, phone in contacts.items():
#title() it captalize the all firsht letters of the name
#         print(f"{name.title()}: {phone}") 
def show_contacts():
    for name in sorted(contacts):
        print(f"{name.title()}: {contacts[name]}")

show_contacts()
add_contact("reshma","903877479379")
add_contact("grishma","8954984983")
# delete_contact("dilli")
# search_contact("manoj")
# search_contact("kumar")




# def delete_contact(name ):
#     if name in contacts:
        # print()








