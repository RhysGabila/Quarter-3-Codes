student = {
    "name" : "?",
    "age" : "!",
    "subject" : "."
}

n = input(print("Enter your name: "))
a = input(print("Enter your age: "))
s = input(print("Enter your favorite subject: "))

student["name"] = n
student["age"] = a
student["subject"] = s

print("Student Record:")
print("Name: ", student["name"])
print("Age: ", student["age"])
print("Favorite Subject: ", student["subject"])
