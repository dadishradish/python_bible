students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for genders in students.keys():
    for name in students[genders]:
        if "a" in name:
            print(name)
