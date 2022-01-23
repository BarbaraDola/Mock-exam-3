from django.core.management import BaseCommand
from student_lecture_app.models import Student

models_data = [
    {
        'name': 'Jack',
        'year_at_university': 5,
        'is_active': False,

    },
    {
        'name': 'Ann',
        'year_at_university': 3,
    },

    {
        'name': 'Robert',
        'year_at_university': 1,
    },

    {
        'name': 'Josephine',
        'year_at_university': 4,
    },
    {
        'name': 'Mike',
        'year_at_university': 2,
    },
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for model_data in models_data:
            student = Student.objects.create(**model_data)
            print(f'{student.name} : {student.year_at_university} - Added')
