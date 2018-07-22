from django.db import models


class IFSC(models.Model):
    ifsc = models.CharField(max_length=12)

    def __str__(self):
        return str(self.pk) + " - " + str(self.ifsc)
