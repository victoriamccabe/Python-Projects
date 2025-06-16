from django.db import models

# Model manager to add custom model behavior if needed

# Custom manager class (even if empty for now)
class UniversityCampusManager(models.Manager):
    pass

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=100)
    # State limited to 2 characters
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    # Connect the custom manager
    objects = UniversityCampusManager()

    # This will show up nicely in the admin list display
    def __str__(self):
        display_Campus = '{0.campus_name} {0.state} {0.campus_id}'
        return "{} {}, {}".format(self.campus_id, self.campus_name, self.state)


    # Meta options control how the model displays in admin
    class Meta:
        verbose_name = 'University Campus'
        verbose_name_plural = 'University Campus'

