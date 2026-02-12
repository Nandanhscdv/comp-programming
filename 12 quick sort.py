n = int(input("Enter number of students: "))
marks = list(map(int, input("Enter marks of students: ").split()))
if len(marks) > 1:
    pivot = marks[0]
    small = []
    big = []
    for i in range(1, len(marks)):
        if marks[i] <= pivot:
            small.append(marks[i])
        else:
            big.append(marks[i])
    marks = sorted(small) + [pivot] + sorted(big)
print("Marks in ascending order: ", marks)