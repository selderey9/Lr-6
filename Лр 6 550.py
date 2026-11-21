countries = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Denmark': 'Copenhagen',
    'China': 'Beijing',
    'Canada': 'Ottawa'
}
temp_list = []
for country, capital in countries.items():
    temp_list.append((capital, country))
temp_list.sort()
sorted_countries = []
for capital, country in temp_list:
    sorted_countries.append((country, capital))
print(sorted_countries)
