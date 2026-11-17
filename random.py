# STRING OPERATIONS
print("STRING OPERATIONS")

str1 = "python"
str2 = "Programming"

print("String 1:", str1)
print("String 2:", str2)
print("Indexing:", str1[0], str1[-1])
print("Slicing:", str2[0:7])
print("Concatenation:", str1 + " " + str2)
print("Repetition:", str1 * 3)
print()


# LIST OPERATIONS
print("LIST OPERATIONS")

list1 = [10, 20, 30, 40]
list2 = [50, 60]

print("list1:", list1)
print("Indexing:", list1[2])
print("Slicing:", list1[1:4])
print("Concatenation:", list1 + list2)
print("Repetition:", list2 * 2)
print()


# TUPLE OPERATIONS
print("TUPLE OPERATIONS")

tuple1 = (100, 200, 300, 400)
tuple2 = (500, 600)

print("Tuple1:", tuple1)
print("Indexing:", tuple1[1])
print("Slicing:", tuple1[0:3])
print("Concatenation:", tuple1 + tuple2)
print("Repetition:", tuple2 * 3)
print()


# DICTIONARY OPERATIONS
print("DICTIONARY OPERATIONS")

student = {
    "Name": "Purvi",
    "Age": "18",
    "Course": "Python"
}

print(student)
print("Access using key:", student["Name"])

student.update({"city": "Pune"})

print("After Update:", student)
print()


# SET OPERATIONS
print("SET OPERATIONS")

set1 = {10, 20, 30}
set2 = {30, 40, 50}

print("Union:", set1 | set2)

set1.add(60)

print("After Add:", set1)
