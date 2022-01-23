from django.core.management import BaseCommand
from student_lecture_app.models import Lecture, Student

class Command(BaseCommand):

    def handle(self, *args, **options):
        lecture_1_id = 1
        student_1_id = 1
        lecture_1 = Lecture.objects.get(id=lecture_1_id)
        student_1 = Student.objects.get(id=student_1_id)

        lecture_2_id = 2
        student_2_id = 2
        lecture_2 = Lecture.objects.get(id=lecture_2_id)
        student_2 = Student.objects.get(id=student_2_id)

        lecture_3_id = 3
        student_3_id = 1
        lecture_3 = Lecture.objects.get(id=lecture_3_id)
        student_3 = Student.objects.get(id=student_3_id)

        lecture_4_id = 4
        student_4_id = 4
        lecture_4 = Lecture.objects.get(id=lecture_4_id)
        student_4 = Student.objects.get(id=student_4_id)

        lecture_5_id = 1
        student_5_id = 5
        lecture_5 = Lecture.objects.get(id=lecture_5_id)
        student_5 = Student.objects.get(id=student_5_id)



        lecture_1.students.add(student_1)
        lecture_2.students.add(student_2)
        lecture_3.students.add(student_3)
        lecture_4.students.add(student_4)
        lecture_5.students.add(student_5)