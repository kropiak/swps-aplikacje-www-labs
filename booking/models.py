from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    MODE_CHOICES = [
        ("online", "Online"),
        ("stacjonarnie", "Stacjonarnie"),
        ("hybrydowo", "Hybrydowo"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default="online")
    price = models.PositiveIntegerField(default=180)
    specializations = models.ManyToManyField(
        Specialization,
        related_name="specialists",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
