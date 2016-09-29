from django.db import models

JOB_AREAS = (
    ('AN', 'Analyst'),
    ('SW', 'Software'),
    ('MA', 'Manager'),
    ('AS', 'Assistant'),
)


class SignUp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(default='hassamhassan.qc@gmail.com',
                             max_length=100)
    password = models.CharField(max_length=100)
    zip_code = models.IntegerField(blank=True, default=54000)
    job_interest = models.CharField(choices=JOB_AREAS, default='Software',
                                    max_length=100)
    owner = models.ForeignKey('auth.User', related_name='signups')

    class Meta:
        ordering = ('first_name',)


class KeyCredential(models.Model):
    api_key = models.CharField(max_length=100)
    remote_addr = models.CharField(max_length=100)
