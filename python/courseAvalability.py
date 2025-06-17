'''
Course Availability Check – Problem Explanaon
'''




def courseAvailability(courses, course):
    if course in courses:
        return "Course is available"
    else:
        return "Course is not available"

n = 5
courses = [
    "Mathematics", "Science", "History", "Physics", "Computer Science"
]
course = "Mathematics"

print(courseAvailability(courses, course))
