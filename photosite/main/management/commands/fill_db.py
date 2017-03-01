from django.core.management.base import BaseCommand
from main.models import *
from datetime import date


class Command(BaseCommand):
    help = 'Initial data for DB'

    def handle(self, *args, **options):
        categorys = [
            {'name': 'PHOTOSETS', 'description': 'Различные фотосеты.'},
            {'name': 'RACES', 'description': 'Репортажные фото с соревнований.'},
            {'name': 'WIP', 'description': 'В процессе обработки.'},
            {'name': 'PHOTO', 'description': 'Фото на разные темы.'}
        ]
        images = [
            {'name': 'somephoto1', 'category': 'PHOTOSETS', 'image': 'photosets.jpg', 'rating': 1,'description':'Фотка1'},
            {'name': 'somephoto2', 'category': 'RACES', 'image': 'reaces.jpg', 'rating': 2,'description':'Фотка1'},
            {'name': 'somephoto3', 'category': 'WIP', 'image': 'wip.jpg', 'rating': 3,'description':'Фотка1'},
            {'name': 'somephoto4', 'category': 'PHOTO', 'image': 'photo.jpg', 'rating': 4,'description':'Фотка1'},
        ]

        Categorymodel.objects.all().delete()
        for category in categorys:
            category = Categorymodel(**category)
            category.save()

        Imagemodel.objects.all().delete()
        for image in images:
            cat_name = image["category"]
            category = Categorymodel.objects.get(name=cat_name)
            image['category'] = category
            image = Imagemodel(**image)
            image.save()
