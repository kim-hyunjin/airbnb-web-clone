from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "세탁기",
            "건조기",
            "아침식사",
            "실내 벽난로",
            "아기 침대",
            "유아용 식탁의자",
            "셀프 체크인",
            "건물 내 무료 주차",
            "헬스장",
            "자쿠지",
            "수영장",
        ]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))

