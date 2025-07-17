import os
import sys
import django
import random
from faker import Faker
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_enrollment_orm.settings')
django.setup()

from enrollments.models import Student, Course, Enrollment

fake = Faker()

# Create Courses
courses_data = [
    ('Mathematics', 'MATH101', 4),
    ('Physics', 'PHY101', 3),
    ('Computer Science', 'CS101', 4),
    ('English', 'ENG101', 2),
    ('Biology', 'BIO101', 3)
]

courses = []
for title, code, credits in courses_data:
    course, created = Course.objects.get_or_create(title=title, code=code, credits=credits)
    courses.append(course)

# Create Students
students = []
for _ in range(20):
    student = Student.objects.create(
        name=fake.name(),
        email=fake.unique.email(),
        gender=random.choice(['Male', 'Female', 'Other']),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=25)
    )
    students.append(student)

# Enroll Students in Random Courses
for student in students:
    selected_courses = random.sample(courses, k=random.randint(1, 3))
    for course in selected_courses:
        Enrollment.objects.get_or_create(
            student=student,
            course=course,
            grade=random.choice(['A+', 'A', 'B+', 'B', 'C', 'F'])
        )

print("✅ Seeded Students, Courses, and Enrollments successfully.")