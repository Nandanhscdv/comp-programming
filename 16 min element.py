try:
    n = int(input("Enter the number of elements: "))
    print(f"Enter the {n} elements: ")
    elements = list(map(int, input().split()))

    if len(elements) != n:
        print(f"Note: You entered {len(elements)} elements instead of {n}.")
    min_element = min(elements)
    print(f"\nThe minimum element is: {min_element}")
except ValueError:
    print("Invalid input. Please enter numeric values")