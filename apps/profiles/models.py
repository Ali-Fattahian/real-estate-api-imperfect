from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "MALE", _("MALE")
    FEMALE = "FEMALE", _("FEMALE")
    OTHER = "OTHER", _("OTHER")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+12125552368"
    )
    about_me = models.TextField(
        verbose_name=_("About Me"), default="Say something about yourself"
    )
    license = models.CharField(
        verbose_name=_("Real Estate License"), max_length=20, blank=True, default=""
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), blank=True, default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.MALE,
        max_length=20,
        blank=True,
    )
    country = CountryField(verbose_name=_("Country"), default="UK", blank=True)
    city = models.CharField(
        verbose_name=_("City"), max_length=100, default="London", blank=True
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text=_("Are you looking to buy a property?"),
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"),
        default=False,
        help_text=_("Are you looking to sell a property?"),
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?")
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
