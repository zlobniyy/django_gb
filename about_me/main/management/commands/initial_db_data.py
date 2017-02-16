from django.core.management.base import BaseCommand
from main.models import Region, Organization, Work, Study, Aboutme
from datetime import date


class Command(BaseCommand):
    help = 'Initial data for DB'

    def handle(self, *args, **options):
        regions = [
            {'name': 'Красноярский край'},
            {'name': 'Новосибирская область'},
            {'name': 'Республика Хакассия'},
            {'name': 'Москва'}
        ]

        organizations = [
            {'name': 'Пионер - лагерь "Солнечный"', 'region': 'Красноярский край', 'site': '','addres':'с.Тесь','phone':'none'},
            {'name': 'Мелкая конторка', 'region': 'Красноярский край', 'site': '','addres':'г.Минусинск','phone':'none'},
            {'name': 'ЗАО "Мегафон"', 'region': 'Новосибирская область', 'site': 'megafonsib.ru','addres':'г.Новосибирск, Красный проспект, 86','phone':'+7 (923) 250-82-81'},
            {'name': 'ЗАО "ЦФТ"', 'region': 'Новосибирская область', 'site': 'cft.ru','addres':'г.Новосибирск, Мусы Джалиля, 11','phone':'+7 (383) 336-49-49'},
            {'name': 'ХТИ КГТУ', 'region': 'Республика Хакассия', 'site': 'khti.sfu-kras.ru','addres':'г.Абакан, Щетинкина, 27','phone':'+7 (3902) 22‒53‒55'},
            {'name': 'Сибинфорцентр', 'region': 'Новосибирская область', 'site': 'sibinfo.ru','addres':'г. Новосибирск, ул. Коммунистическая, 48а, офис 515','phone':'+7 (383)36-200-36'},
            {'name': 'Опыт', 'region': 'Новосибирская область', 'site': '','addres':'none','phone':'none'},
            {'name': 'GeekBrains', 'region': 'Москва', 'site': 'geekbrains.ru','addres':'Москва, Ленинградский просп., 39, стр. 6','phone':'8 (800) 505‑61-05'}
        ]
        works = [
            {'organization': 'Пионер - лагерь "Солнечный"', 'region': 'Красноярский край', 'site': '',
             'position': 'Вожатый отряда', 'duties': 'Обеспечение досуга и контроль детей', 'period': '3'},
            {'organization': 'Мелкая конторка', 'region': 'Красноярский край', 'site': '',
             'position': 'Мастер починки сотовых телефонов', 'duties': 'Починка сотовых телефонов', 'period': '5'},
            {'organization': 'ЗАО "Мегафон"', 'region': 'Новосибирская область', 'site': 'megafonsib.ru',
             'position': 'Сервисный инженер', 'duties': 'Поддержка пользователей', 'period': '12'},
            {'organization': 'ЗАО "Мегафон"', 'region': 'Новосибирская область', 'site': 'megafonsib.ru',
             'position': 'Системный администратор',
             'duties': 'Обеспечение работоспособности промышленного Active Directory', 'period': '12'},
            {'organization': 'ЗАО "ЦФТ"', 'region': 'Новосибирская область', 'site': 'cft.ru',
             'position': 'Инженер сопровождения', 'duties': 'Поддержка пользователей сервиса денежных переводов',
             'period': '24'},
            {'organization': 'ЗАО "ЦФТ"', 'region': 'Новосибирская область', 'site': 'cft.ru',
             'position': 'Инженер прикладного сопровождения сервиса',
             'duties': 'Анализ работы сервиса денежных переводов и постановка задач на доработку и исправление дефектов',
             'period': '24'},
            {'organization': 'ЗАО "ЦФТ"', 'region': 'Новосибирская область', 'site': 'cft.ru',
             'position': 'Инженер прикладного администрирования', 'duties': 'Инженер прикладного администрирования',
             'period': '24'},
            {'organization': 'ЗАО "ЦФТ"', 'region': 'Новосибирская область', 'site': 'cft.ru',
             'position': 'Инженер прикладного сопровождения банковской системы',
             'duties': 'Поддержка пользователей банковской системы', 'period': '30'}
        ]

        hobbies = [
            {'hobbyname': 'Фехтование', 'hobbylevel': '6', 'period': '120'},
            {'hobbyname': 'Фотография', 'hobbylevel': '2', 'period': '48'},
            {'hobbyname': 'Автоспорт', 'hobbylevel': '2', 'period': '999'},
            {'hobbyname': 'Автомобили', 'hobbylevel': '4', 'period': '999'},
            {'hobbyname': 'Программирование', 'hobbylevel': '2', 'period': '6'}
        ]

        studies = [
            {'organization': 'ХТИ КГТУ', 'site': 'khti.sfu-kras.ru', 'region': 'Республика Хакассия',
             'course': 'Высшее техническое образование по автоматизации проектирования в машиностроении',
             'period': '60'},
            {'organization': 'Сибинфорцентр', 'site': 'sibinfo.ru', 'region': 'Новосибирская область',
             'course': 'Oracle DBA level 1', 'period': '1'},
            {'organization': 'Сибинфорцентр', 'site': 'sibinfo.ru', 'region': 'Новосибирская область',
             'course': 'Oracle DBA level 2', 'period': '1'},
            {'organization': 'Сибинфорцентр', 'site': 'sibinfo.ru', 'region': 'Новосибирская область',
             'course': 'Oracle SQL Tuning',
             'period': '1'},
            {'organization': 'Сибинфорцентр', 'site': 'sibinfo.ru', 'region': 'Новосибирская область',
             'course': 'Linux(Debian-family)', 'period': '1'},
            {'organization': 'Опыт', 'site': '', 'region': 'Новосибирская область', 'course': 'Unix Solaris',
             'period': '48'},
            {'organization': 'Сибинфорцентр', 'site': 'sibinfo.ru', 'region': 'Новосибирская область',
             'course': 'Shell(Bash)',
             'period': '1'},
            {'organization': 'GeekBrains', 'site': 'geekbrains.ru', 'region': 'Москва', 'course': 'HTML/CSS+Bootstrap',
             'period': '1'},
            {'organization': 'GeekBrains', 'site': 'geekbrains.ru', 'region': 'Москва', 'course': 'Javascript',
             'period': '1'},
            {'organization': 'GeekBrains', 'site': 'geekbrains.ru', 'region': 'Москва', 'course': 'Python3', 'period': '1'},
            {'organization': 'GeekBrains', 'site': 'geekbrains.ru', 'region': 'Москва', 'course': 'Django', 'period': '1'}
        ]

        Region.objects.all().delete()
        for region in regions:
            region = Region(**region)
            region.save()

        Organization.objects.all().delete()
        for organization in organizations:
            reg_name = organization["region"]
            region = Region.objects.get(name=reg_name)
            organization['region'] = region
            organization = Organization(**organization)
            organization.save()

        Work.objects.all().delete()
        for work in works:
            org_name = work["organization"]
            reg_name = work["region"]
            region = Region.objects.get(name=reg_name)
            organization = Organization.objects.get(name=org_name)
            work['organization'] = organization
            work['region'] = region
            work = Work(**work)
            work.save()

        Aboutme.objects.all().delete()
        for hobby in hobbies:
            hobby = Aboutme(**hobby)
            hobby.save()

        Study.objects.all().delete()
        for study in studies:
            org_name = study["organization"]
            reg_name = study["region"]
            region = Region.objects.get(name=reg_name)
            organization = Organization.objects.get(name=org_name)
            study['organization'] = organization
            study['region'] = region
            study = Study(**study)
            study.save()
