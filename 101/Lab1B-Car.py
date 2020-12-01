acceleration = 0
time = 0
print("Input the amount of time required for the car to reach 60mph, in seconds.")
print("TIME>", end=" ")
time = float(input()) / 3600.0
acceleration = 60.0 / time
print("The acceleration of the car is (in miles/hour^2):")
print("OUTPUT", round(acceleration))
