playlist=['shape of you','naa ready','believer','tum hi ho']
favourite_food=['pizza','burger','dhosa','biriyani']
location=['home','mall','work','airport']

#list methons
#append
playlist.append('oo antava')
print('after append',playlist)

#insert
playlist.insert(1,'song for mk')
print('after insert',playlist)

#remove
playlist.remove('naa ready')
print('after remove',playlist)


#pop
playlist.pop()
print('after pop',playlist)

#reverse
playlist.reverse()
print('after reverse',playlist)

#count
print('count',playlist.count('believer'))


#list slicing
print('all places',location)
print('2 places',location[0:2])
print('last 2 places',location[-2:])


#list iteration
print('favourite food',favourite_food)
for food in favourite_food:
    print('all food',food)

for song in playlist:
    print(song+ ' by mathan')


#check if item exist
if 'dhosa' in favourite_food:
    print('yes item in the list')