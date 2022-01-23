from django.core.management import BaseCommand
from student_lecture_app.models import Lecture

models_data = [
    {
        'name': 'Economy',
        'lecturer': 'Jacek Józwiszyn',
    },
    {
        'name': 'Statistics',
        'lecturer': 'Walenty Ostasiewicz',
    },
    {
        'name': 'Algebra',
        'lecturer': 'Janusz Łyko ',
    },
    {
        'name': 'Econometrics',
        'lecturer': 'Jerzy Nowiński',
    },
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for model_data in models_data:
            lecture = Lecture.objects.create(**model_data)
            print(f'{lecture.name}, {lecture.lecturer} added.')