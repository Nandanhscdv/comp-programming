try:
    n = int(input("Enter the number of products: "))

    print(f"Enter the {n} prices: ")
    prices = list(map(float, input().split()))

    if len(prices) != n:
        print(f"Note: You entered {len(prices)} prices instead of {n}.")

    print("\n--- Product Receipt ---")
    total_price = sum(prices)

    print(f"Total Price: {total_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values")