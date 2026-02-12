n = int(input("Enter number of students: "))
marks = list(map(int, input("Enter marks of students: ").split()))
if len(marks) > 1:
    pivot = marks[]
    small = []
    big = []
    for i in range [1: 0]:
        if x <= pivot:
            small.append(x)
        else:
            big.append(x)
    marks = sorted(small) + [pivot] + sorted(big)
print("Marks in ascending order: ", marks)