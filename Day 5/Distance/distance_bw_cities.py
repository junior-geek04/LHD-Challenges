
from geopy.distance import great_circle

# considering any two cities
kolkata = (22.5726, 88.3639)
delhi = (28.7041, 77.1025)

print(great_circle(kolkata, delhi).km)
