def interactive_hash_lookup():
    # 1. Initialize the Hash Table (Set)
    dataset = set()
    
    # 2. Get number of strings to store
    try:
        n = int(input("Enter the number of strings to store: "))
        print(f"Please enter {n} strings (one per line):")
        for i in range(n):
            item = input(f" {i+1}: ").strip()
            dataset.add(item)
            
        # 3. Get number of queries
        q = int(input("\nEnter the number of lookup queries: "))
        print(f"Please enter {q} query strings:")
        
        results = []
        for i in range(q):
            query = input(f" Query {i+1}: ").strip()
            if query in dataset:
                results.append("found")
            else:
                results.append("not found")
        
        # 4. Display results
        print("\n--- Results ---")
        for res in results:
            print(res)
            
    except ValueError:
        print("Invalid input. Please enter integers for counts.")

if __name__ == "__main__":
    interactive_hash_lookup()