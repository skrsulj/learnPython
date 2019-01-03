
# boolean and none
print("*" * 40)
print("boolean or none")
print("*" * 40)

python_course = True
java_course = False

print(f"INT Vlaue of python_course is {int(python_course)}")
print(f"INT Vlaue of java_course is {int(java_course)}")
print(f"String Vlaue of python_course is {str(python_course)}")
print(f"String Vlaue of java_course is {str(java_course)}")

aliens_found = None

print(f"INT Vlaue of aliens_found is {str(aliens_found)}")

# Lists
print("*" * 40)
print("If statements")
print("*" * 40)


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
print("*" * 40)
print("Lists")
print("*" * 40)

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

# Loops *************************************
print("*" * 40)
print(" For Loops")
print("*" * 40)

for name in student_names:
    print(f"Student name is {name}")

x = 0
for index in range(10):
    x += 10
    print( "The value of X is {0}".format(x) )

for index in range(5, 10):
    print( "The value of index is {0}".format(index) )
    
for index in range(5, 10, 2):
    print( "The value of index is {0}".format(index) )


# Break and Continue *************************************
print("*" * 40)
print("Break and Continue")
print("*" * 40)

student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

print(" # break if found Mark example ")
for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break
    else:
        print("Currently testing " + name)

print(" # continue if found Bort example ")
for name in student_names:
    if name == "Bort":
        continue
    print("Currently testing " + name)


# While Loops *************************************
print("*" * 40)
print(" While Loops")
print("*" * 40)

x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1


# infinite loop

num = 10
while True:
    if num == 42:
        break
    print("Hello World {0}".format(num))
    num += 2


# Dictionaries *************************************
print("*" * 40)
print(" Dictionaries ")
print("*" * 40)


student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None
}

print( student["name"] )
print( student.get("last_name", "Unknown") )

all_students = [
    {"name" : "Mark", "student_id" : 15163 },
    {"name" : "Katarina", "student_id" : 63112 },
    {"name" : "Jessica", "student_id" : 30021 }
    ]

print( student.keys() )
print( student.values() )

student["name"] = "James"

print( student.values() )

del student["name"]

print( student.values() )


# Exceptions *************************************
print("*" * 40)
print(" Exceptions ")
print("*" * 40)

student["last_name"] = "Kowalski"
try:
    last_name = student["last_names"]
    numbered_last_name = 3 + last_name
##except KeyError:
##    print("Error finding last_name")
##except TypeError as error:
##    print("I can't add these two together")
##    print(error)
except Exception as error:
    print("Unknown Error")
    print(error)

print("Finished checking for last_name")






















