import re

data = input()
locations = []
travel_points = 0

pattern = r'(=|/)([A-Z][a-zA-Z]{2,})\1'

matches = re.findall(pattern, data)

for location in matches:
    travel_point = len(location[1])
    travel_points += travel_point
    locations.append(location)

print(f"Destinations: {', '.join(location[1] for location in locations)}")
print(f"Travel Points: {travel_points}")
