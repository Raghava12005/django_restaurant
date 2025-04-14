from django.db import models


CHOICES = [
    ('1', 'definitely'),
    ('2', 'maybe'),
    ('3', 'not sure')
]

rolech = [
    ('1', 'individual'),
    ('2', 'couple'),
    ('3', 'small group'),
    ('4', 'large group'),
    ('5', 'prefer not to say')
]

pur = [
    ('1', 'Date'),
    ('2', 'Birthday'),
    ('3', 'Anniversary'),
    ('4', 'Party')
]


class table(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=230)
    email = models.EmailField(max_length=254)
    time = models.CharField(max_length=12, default='')
    phone = models.CharField(max_length=30, default='')
    people = models.IntegerField(default=1)
    message = models.TextField(max_length=300, null=True, blank=True)

    # 🆕 Additional fields to match your form/view
    age = models.IntegerField(null=True, blank=True)
    prefer = models.CharField(choices=CHOICES, max_length=20, null=True, blank=True)
    role = models.CharField(choices=rolech, max_length=20, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    purpose = models.CharField(choices=pur, max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
