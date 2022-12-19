class Student():
    number = 100000
    university = "UEK Kraków"

    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.number = Student.number
        Student.number += 1
        self.field_of_study = field_of_study

    def __str__(self):
        return f"{self.name} {self.surname}, ({self.number}), {self.field_of_study}, {Student.university}"

student1 = Student("Anna", "MAJ", "Applied informatics")
print(student1)

student2 = Student("Jan", "Kowalski", "Zarządzanie w biznesie")
print(student2)

student3 = Student("Andrzej", "Nowak", "Informatyka stosowana")
print(student3)
