from django.db import models
from adzmart.base_model import BaseModel

# define some constants to double check requests and db representations.
MEDIA_TYPE = (
        ('Outdoor', 'Outdoor'),
        ('Radio', 'Radio'),
        ('Television', 'Television'),
        ('Print', 'Print'),
        ('Mobile', 'Online/Mobile'),
        ('Cinema', 'Cinema'),
        ('Other', 'Other')
    )


CONTACT_METHOD = (
        ("Phone", "Phone"),
        ("Email", "Email"),
    )

AD_BUDGET = (
    ('N200,000 - N500,000', 'N200,000 - N500,000'),
    ('N500,000 - N1,000,000', 'N500,000 - N1,000,000'),
    ('N1,000,000 - N2,000,000', 'N1,000,000 - N2,000,000'),
    ('N1,000,000 - N2,000,000', 'N1,000,000 - N2,000,000'),
)

AD_EXPERIENCE = (
    ('I have already booked advertising myself several times', 'I have already booked advertising myself several times'),
    ('So far I have only booked advertising through agencies', 'So far I have only booked advertising through agencies'),
    ('I want to book advertising for the first time', 'I want to book advertising for the first time'),
    ('I have no experience so far and only need information at first', 'I have no experience so far and only need information at first')

)

STATUS = (
    ('Opened', 'Opened'),
    ('Processing' , 'Processing'),
    ('Completed', 'Completed'),
)

class CustomerInfo(BaseModel):
    """
    A common interface defining customer information and RFP status for models in the done-for-me module.
    """
    status = models.CharField(max_length=50, choices=STATUS, default='Opened')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    is_existing_customer = models.BooleanField(default=False)
    preferred_contact_method = models.CharField(max_length=50, choices=CONTACT_METHOD)

    class Meta():
        abstract = True


class MediaBrief(CustomerInfo):
    """
    Handles media quote for done-for-me customer.
    """
    campaign_details = models.TextField()
    target_audience = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    duration = models.TextField()
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPE)

    class Meta:
        verbose_name_plural = 'Media Briefs'

    def __str__(self):
        return self.company_name


class MediaAdvisory(CustomerInfo):
    """
    Handles media advisory for done-for-me customer.
    """ 
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPE)
    planned_budget = models.CharField(max_length=50, choices=AD_BUDGET,)
    advertising_experience = models.CharField(max_length=255, choices=AD_EXPERIENCE)
    additional_info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Media Advisory'

    def __str__(self):
        return self.company_name

    
class Support(CustomerInfo):
    """
    Handles media support queries for a do-for-me customer.
    """
    request_info = models.TextField()

    class Meta:
        verbose_name_plural = 'Support'

    def __str__(self):
        return self.company_name
