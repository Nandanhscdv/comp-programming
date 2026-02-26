n = int(input("Enter number of cars: "))
distances = list(map(int, input("Enter distance of cars: ").split()))

left = 0
right = n - 1
result = []

while left <= right:
    if left == right:
        result.append(distances[left])
    else:
        result.append(distances[left])
        result.append(distances[right])
    
    left += 1
    right -= 1

print("Processed Order:", *result)