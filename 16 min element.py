try:
    n = int(input("Enter the number of elements: "))
    print(f"Enter the {n} elements: ")
    elements = list(map(int, input().split()))

    if len(elements) != n:
        print(f"Note: You entered {len(elements)} elements instead of {n}.")
    
    if n > 0:
        min_element = elements[0]
        
        for i in range(1, len(elements)):
            if elements[i] < min_element:
                min_element = elements[i] 
        print(f"\nThe minimum element is: {min_element}")
    else:
        print("The list is empty.")

except ValueError:
    print("Invalid input. Please enter numeric values")