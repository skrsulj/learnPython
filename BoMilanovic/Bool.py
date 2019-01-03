
# boolean and none

python_course = True
java_course = False

print(f"INT Vlaue of python_course is {int(python_course)}")
print(f"INT Vlaue of java_course is {int(java_course)}")
print(f"String Vlaue of python_course is {str(python_course)}")
print(f"String Vlaue of java_course is {str(java_course)}")

aliens_found = None

print(f"INT Vlaue of aliens_found is {str(aliens_found)}")



number = 6

if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

# truthy values

text = "Python"

if number:
    print("Number is defined and tuthy")

if text:
    print("Text is defined and truthy")

# falsy value
print("falsy value")

if java_course:
    print("This is falsy and should not print")

if aliens_found:
    print("This is falsy and should not print")

# Not if
print("Not if")

number = 5

if number != 5:
    print("This will not execute")

python_course = True
# truthy falsey
if not python_course:
    print("This will not execute")


# Ternary if statements
print("Ternary if statements")

a = 1
b = 2

print( "bigger" if a < b else "smaller" )


# Lists
print("Lists")

student_names = [] # empty list
student_names = ["Mark", "Katarina", "Jessica"]

print(student_names[0])
print(student_names[2])
print(student_names[-1])

print(student_names)
student_names[0] = "James"
print(student_names)

# student_names[3] = "Homer"  # will not work
student_names.append("Homer")  # add to the end

print(student_names)
print( "Katarina" in student_names )

print( len(student_names) )  #How many elements in the list

del student_names[2]
print( len(student_names) )
print(student_names)

print("List Slicing")
print( student_names[1:] )
print( student_names[1:-1] )




















