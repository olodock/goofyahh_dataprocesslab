import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("ALL CITIES IN GERMANY")
for city in cities:
    if city['country'] == "Germany":
        print(city['city'])
print()

# Print all cities in Spain with a temperature above 12°C
print("ACISWATA12C")
for city in cities:
    if city['country'] == "Spain":
        if float(city['temperature']) > 12:
            print(city["city"])
print()
# Count the number of unique countries
countries = []
print("CTNOUC")
for city in cities:
    countries.append(city['country'])
print(len(set(countries)))
print()
# Print the average temperature for all the cities in Germany
print()
def PTATFATCG():
    print("PTATFATCG")
    temps = []
    for c in cities:
        if c['country'] == "Germany":
            temps.append(float(c['temperature']))
    print(sum(temps)/len(temps))
PTATFATCG()
# Print the max temperature for all the cities in Italy
print()
def PTMTFATCII():
    print("PTMTFATCII")
    temps = []
    for c in cities:
        if c['country'] == "Italy":
            temps.append(float(c['temperature']))
    print(max(temps))
PTMTFATCII()