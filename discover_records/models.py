from django.db import models


class Record(models.Model):
    """
    Model to hold minimal set of TNA record data.
    """

    id = models.CharField(max_length=36, primary_key=True)
    title = models.CharField(max_length=250, blank=True)
    scope_content_description = models.CharField(max_length=500, blank=True)
    citable_reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.id
