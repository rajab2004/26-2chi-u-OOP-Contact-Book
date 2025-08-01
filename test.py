import json
from contact import Contact


contact = Contact(name='Vali', phone="991231212", email="vali@gmail.com")
print(contact.contact_id)


with open('contacts.json') as jsonfile:
    data_list = json.load(jsonfile)

contacts: list[Contact] = []
for data in data_list:
    contacts.append(Contact.from_dict(data))

for contact in contacts:
    print(contact.to_dict())

