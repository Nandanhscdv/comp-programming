n = int(input("Enter number of finishing times: "))
arr = list(map(int, input("Enter finishing times: ").split()))
if len(arr) != n:
    print("Number of finishing times does not match the specified count.")
    exit(1)
result = 0
print(f"Finishing times: {arr}")