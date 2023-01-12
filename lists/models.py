import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core import models as core_model


class List(core_model.TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE, default=uuid.uuid1
    )

    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = _("Number of Rooms")
