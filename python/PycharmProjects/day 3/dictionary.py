#dictionary method
trip={
    'trip_id':'ub12345',
    'pickup':'Chennai central',
    'drop':'airport',
    'fair':430.75,
    'driver':'ravi',
    'status':'completed'
}
print(trip)
print(trip['drop'])

print(trip.get('airport'))
print(trip.keys())
print(trip.values())


for key,value in trip.items():
    print(key,':',value)
