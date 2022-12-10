from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    def handle(self, *args, **options):

        amenities = [
            "Air conditioning",
            "Alarm clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee maker in romm",
            "Cooking hob",
            "Cookware & kitchen utensils",
            "Dishwasher",
            "Double bed",
            "En suit bathroom",
            "Free parking",
            "Free wireless internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair dryer",
            "Heating",
            "Hot tub",
            "Indoor pool",
            "Ironing board",
            "Microwave",
            "Outdoor pool",
            "Outdoor tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towel",
            "TV",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
