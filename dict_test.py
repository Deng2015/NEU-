people = {
    "Alice":{
        "phone": 1234,
        "addr": "Rockland 23"
    },
    "Bob":{
        "phone": 2344,
        "addr": "Kim str 24"
    }
}

labels = {
    "phone": "phone number",
    "addr": "address"
}
name = input("Input the name: \n")
request = input ("Phone number(p) or address(a)?\n")

if request == "p":
    key = "phone"
if request == "a":
    key = "addr"

if name in people:
    print("{}'s {} is {}.".format(name,labels[key],people[name][key]))
