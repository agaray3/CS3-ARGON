"""Association (Knows-a): Student <-> Course (many-to-many).

Both objects are independent and keep references to each other, but
neither owns the other. Deleting one does not destroy the other.
"""


class Course:
    def __init__(self, code: str, title: str):
        self.code = code
        self.title = title
        self.students = []  # Course knows its Students


class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []  # Student knows its Courses

    def enroll(self, course: Course):
        # Establish the link in BOTH directions
        self.courses.append(course)
        course.students.append(self)


if __name__ == "__main__":
    ana = Student("Ana")
    ben = Student("Ben")

    oop = Course("CS102", "Object-Oriented Programming")
    db = Course("CS103", "Database Systems")

    ana.enroll(oop)
    ana.enroll(db)
    ben.enroll(oop)

    print(f"{ana.name}'s courses: {[c.code for c in ana.courses]}")
    print(f"{ben.name}'s courses: {[c.code for c in ben.courses]}")
    print(f"{oop.code} enrollees: {[s.name for s in oop.students]}")
    print(f"{db.code} enrollees: {[s.name for s in db.students]}")
