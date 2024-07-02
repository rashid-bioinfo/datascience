# setting dictionary comprehesion
# Suppose we have two dictionaries one is for cities and other is for countries, 
# now we want to make cities as 'keys' and countries as 'values'

countries = ['Pakistan', 'India', 'Bangladesh', 'Saudi Arabia']
cities = ['Islambad', 'Delhi', 'Daka', 'Rayadh']
z = zip(cities, countries)
for i in z:
    print(i)

# OR the short way
# we will use set instead of list in order to get rid of duplicate values
combined_dict = {city:country for city,country in zip(cities, countries)}
print(combined_dict)