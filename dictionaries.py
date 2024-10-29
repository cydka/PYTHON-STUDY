person={
    'name':"verah",
    'age':19,
    'gender':"female",
    'location':["kiambu",518,"thika"],
    'address':{
        'street':'muthaiga',
        'city':"nairobi",
        'county':"kenya"

    }
}
print(type(person))
print(person)


# use key to display certain values bcoz its unordered
print(person['name'])
print(person['age'])
print(person['gender'])
print(person['location'][1])
# display thika
print(person['location'][2])


print(person['address']['street'])
print(person['address']['city'])
print(person['address']['county'])
# update values
person['age']=40
# add new key and value
person['occupation']="engineer"
print(person)


# dictionary methods  .keys is used to return all the keys
print (person.keys())
# . values returns all the values in a dictionary
print(person.values())


# .items returns a list containing list and values inside a tuple
print(person.items())

# .pop is used to remove the value with specified key
person.pop('name')
# remove occupation
person.pop('occupation')
print(person)

# get returns value of specified key
print(person.get('address'))

