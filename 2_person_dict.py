#
person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)
#print(person["children"][1])

#print(person['pets']['cat'])

for a in person['children']:
    print(a)

for b in person["pets"]:
    print(person['pets'][b])
