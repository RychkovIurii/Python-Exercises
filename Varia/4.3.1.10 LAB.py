def liters_100km_to_miles_gallon(liters):
    count_of_gal = liters / 3.785411784
    count_of_miles = 100 / 1.609344
    return count_of_miles / count_of_gal

def miles_gallon_to_liters_100km(miles):
    count_of_km = miles * 1.609344
    count_of_liters = 3.785411784
    return count_of_liters * 100 / count_of_km
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
