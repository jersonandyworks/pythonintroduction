import math
import time
feet = 800 #ft
seconds = 25 #seconds
degreeX = math.radians(65)
degreeY = math.radians(20)
delay = 1.5
x = round(feet / math.tan(degreeX),2)
y = round(feet / math.tan(degreeY),2)

if x > y:
    distance = x - y
else:
    distance = y - x
print("Distance X: " + str(x))
time.sleep(delay)
print("Distance Y: " + str(y))
time.sleep(delay)
print ("Total Distance: " + str(distance))
time.sleep(delay)
distancePerSecond = round(distance / seconds,2)
print(str(distancePerSecond) + " ft/s")
time.sleep(delay)
distancePerHour = round(distancePerSecond * 60 * 60,2)

print(str(distancePerHour) + " ft/hr")
time.sleep(delay)

kilometerPerHour = round(distancePerHour / 3280.84,2) # 1km = 3280.84 feet
milesPerHour = round(distancePerHour / 5280) # 1 mile = 5280 feet
print(str(kilometerPerHour) + " km/hr")
time.sleep(delay)
print(str(milesPerHour) + " mi/hr")