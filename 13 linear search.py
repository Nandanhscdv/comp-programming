n = list(map(int, input("Enter the number: ").split()))
x = int(input("Enter the element: "))
result = -1
for i in range(len(n)):
    if (n[i] == x):
        result = i
if result == -1:
    print("Element not found in the array.")
else:
    print(f"Element found at index: {result}")