#set order
uber_cities=['chennai','banglore','chennai','delhi','banglore']

unique_cities=set(uber_cities)
print(unique_cities)

ola_city1={'chennai','banglore','hyd'}
ola_city2={'delhi','banglore','madurai'}

print(ola_city1.union(ola_city2))
print(ola_city1.intersection(ola_city2))

print(ola_city2.difference(ola_city1))

ola_city1.add('karur')
ola_city2.remove('delhi')
print(ola_city1,ola_city2)