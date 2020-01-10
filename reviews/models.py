from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    VERY_BAD = 1
    BAD = 2
    SOSO = 3
    GOOD = 4
    BEST = 5

    RATING_CHOICES = [
        (VERY_BAD, "1"),
        (BAD, "2"),
        (SOSO, "3"),
        (GOOD, "4"),
        (BEST, "5"),
    ]

    review = models.TextField()
    accuracy = models.IntegerField(choices=RATING_CHOICES)
    communication = models.IntegerField(choices=RATING_CHOICES)
    cleanliness = models.IntegerField(choices=RATING_CHOICES)
    location = models.IntegerField(choices=RATING_CHOICES)
    check_in = models.IntegerField(choices=RATING_CHOICES)
    value = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 1)
