driver_name='mk mathan'

print(driver_name.lower())
print(driver_name.upper())
print(driver_name.capitalize())

mobile='6369482415'
masked=mobile[:2]+'********'+mobile[-2:]
print(masked)

song='shap OF you'
artist='mk MATHAN'
formatted=f'{song.title()} - {artist.title()}'
print(formatted)

location='chennai central'
fixed_location=location.replace('chennai central','salem')
print(fixed_location)

message='your id is;UB4567.please keep it safe'
booking_id=message.split(';')[1].split('.')[0].strip()
print(booking_id)

