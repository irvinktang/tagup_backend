from django.db import models


class Record(models.Model):
    creationDate = models.FloatField(help_text='Unix time in milliseconds')
    lastModificationDate = models.FloatField(
        help_text='Unix time in milliseconds',
    )
    timestamp = models.FloatField(help_text='Unix time in milliseconds')
    value1 = models.CharField(max_length=200)
    value2 = models.FloatField()
    value3 = models.BooleanField(default=False)

    def __str__(self):
        return str({
            'creationDate': self.creationDate,
            'lastModificationDate': self.lastModificationDate,
            'timestamp': self.timestamp,
            'value1': self.value1,
            'value2': self.value2,
            'value3': self.value3,
        })
