from django.db import models
from accounts.models import Account


class Prayer(models.Model):

    """
    The main Prayer object which holds data about both requests and
    praises
    """

    PRAYER_TYPE = (
        ('praise', 'Praise'),
        ('request', 'Request')
    )

    PRIVACY_CHOICES = (
        ('public', 'Available to Public'),
        ('protected', 'Available to Registered User'),
        ('prayer_team', 'Available to Prayer Team'),
        ('staff', 'Available to Church Staff'),
    )

    STATUS_CHOICES = (
        ('automatic_approval', 'Automatically Approved (Verified Account)'),
        ('approved', 'Approved After Review'),
        ('awaiting_approval', 'Waiting For Approval'),
    )

    prayer_type = models.CharField(choices=PRAYER_TYPE, max_length=100)
    prayer_contents = models.TextField()
    prayer_privacy = models.CharField(choices=PRIVACY_CHOICES, max_length=100)
    requester = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    allow_support = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.requester)

    class Meta:
        verbose_name = 'Prayer'
        verbose_name_plural = 'Prayers'


class PrayerSupport(models.Model):

    """
    The PrayerSupport model denotes support made for a Prayer object
    """

    SUPPORT_TYPES = (
        ('praying', 'Praying for your request!'),
        ('praising', 'Praising along side you!'),
    )
    
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    support_type = models.CharField(choices=SUPPORT_TYPES, max_length=100)
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sender)

    class Meta:
        verbose_name = 'Prayer Support Action'
        verbose_name_plural = 'Prayer Support Actions'