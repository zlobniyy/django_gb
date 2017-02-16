from django.core.management.base import BaseCommand
from mainapp.models import Work, Hobby, Study, Organization
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organizations = [
            {'name': 'WebDev1', 'region': 'Урал', 'tax_id': 123456, 'site': 'webdev1.local'},
            {'name': 'WebDev2', 'region': 'Урал', 'tax_id': 654321, 'site': 'webdev2.local'},
            {'name': 'GeekBrains', 'region': 'Москва', 'tax_id': 123456, 'site': 'geekbrains.ru'},

        ]
        works = [
            {'organization': 'WebDev1', 'position': 'Программист-разработчик',
             'duties': 'Разработка веб-сервисов.Написание '
                       'кода.Верстка по предоставленным '
                       'макетам (Bootstrap)', 'period': 12},
            {'organization': 'WebDev2', 'position': 'Программист Python',
             'duties': 'Доработка функциональности сайта.'
                       'Верстка по предоставленным шаблонам.', 'period': 6},
            {'organization': 'GeekBrains', 'position': 'Преподаватель',
             'duties': 'Подготовка и преподавание курсов', 'period': 18},
        ]
        hobbies = [
            {'name': 'сноуборд'},
            {'name': 'фотография'},
        ]
        studies = [
            {'type': 'school', 'number': 111,
             'study_from': date(1987, 9, 1), 'study_to': date(1995, 6, 1)},
            {'type': 'lyceum', 'number': 222,
             'study_from': date(1995, 9, 1), 'study_to': date(1997, 6, 1)},
            {'type': 'university', 'number': 0,
             'study_from': date(1997, 9, 1), 'study_to': date(2002, 8, 1)},
        ]

        Organization.objects.all().delete()
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()

        Work.objects.all().delete()
        for work in works:
            org_name = work["organization"]
            # Получаем организацию по имени
            organization = Organization.objects.get(name=org_name)
            # Заменяем название организации объектом
            work['organization'] = organization
            work = Work(**work)
            work.save()

        Hobby.objects.all().delete()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()

        Study.objects.all().delete()
        for study in studies:
            study = Study(**study)
            study.save()
