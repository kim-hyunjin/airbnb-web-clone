from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command creates amenities"

    # def add_arguments(self, parser):

    #   parser.add_argument("--times", help="How many times do you want me to tell you that I love you?")

    def handle(self, *args, **options):
        amanities = [
            "주방",
            "샴푸",
            "난방",
            "에어컨",
            "무선 인터넷",
            "옷걸이",
            "다리미",
            "헤어드라이어",
            "노트북 작업 공간",
            "TV",
            "욕실 단독 사용",
        ]
        for a in amanities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))

