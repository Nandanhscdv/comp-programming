n = int(input("Enter number of cars: "))
distances = list(map(int, input("Enter distances of n cars: ").split()))
speeds = list(map(int, input("Enter speeds of n cars: ").split()))

min_speed = speeds[0]

for speed in speeds:
    if speed < min_speed:
        min_speed = speed

max_dist = distances[n-1]
max_time = max_dist / min_speed

print(f"slowest speed: {min_speed}")
print(f"Maximum time: {max_time:.2f}")