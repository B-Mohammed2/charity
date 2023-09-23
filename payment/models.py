# from django.contrib.auth.models import User
import uuid
from django.db import models
from django.conf import settings
# from django_countries.fields import CountryField  # importing django-countries

from charity_hub.models import Charity  # Import the Charity model
# from your_app_name.models import UserProfile  # Import the UserProfile model

class donation_payment(models.Model):
    donation_number = models.CharField(max_length=30, null=False, editable=False)
    # user_profile = models.ForeignKey(user_profile, on_delete=models.SET_NULL,
    #                                  null=True, blank=True,
    #                                  related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField (max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    donation_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

  
    # stripe_pid = models.CharField(max_length=254, null=False, blank=False,
    #                               default='')

     # from code instute
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.donation_number:
            self.donation_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donation_number



class donation_detail(models.Model):
    donation_payment = models.ForeignKey(donation_payment, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='lineitems')
    charity_name = models.ForeignKey(Charity, null=False, blank=False,
                                     on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=6, decimal_places=2,
                                          null=False, blank=False,
                                          editable=False)


   

# New model for subscriptions
# class Subscription(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     plan = models.CharField(max_length=50)  # Store the plan identifier from the payment gateway
#     status = models.CharField(max_length=20)  # Active, canceled, etc.
#     start_date = models.DateField()
#     end_date = models.DateField()