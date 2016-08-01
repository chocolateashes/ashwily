gwc_lockheed = [  4, 5, 9, 1, 2, 8, 3, 10, 7, 6 ]

print("Before sort: ")
print(gwc_lockheed)

print("----------- Sorting ----------- ")

def bubble_sort_students(student_numbers):
    for student in range(len(student_numbers) -1, 0, -1):
        for number in range(student):
            if student_numbers[number] > student_numbers[number + 1]:
                temporary = student_numbers[number]
                student_numbers[number] = student_numbers[number + 1]
                student_numbers[number + 1] = temporary
    return student_numbers

print("After sort:")
bubble_sort_students(gwc_lockheed)
print(gwc_lockheed)
print("Ashwini is awesome!")


