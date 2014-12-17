from django.db import models


class NEAL_model(models.Model):
    #one=models.CharField(max_length=200)
    #two=models.CharField(max_length=200)
    object_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    url_audio_file = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_learned = models.DateTimeField()
    confidence = models.DecimalField(max_digits = 4, decimal_places = 3)
    def __unicode__(self):
        return self.object_name


class NEAL_download_model(models.Model):
    #one=models.CharField(max_length=200)
    #two=models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    object_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    url_audio_file = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    #start_time = models.DateTimeField()
    #end_time = models.DateTimeField()
    date_learned = models.DateTimeField()
    #confidence = models.DecimalField(max_digits = 4, decimal_places = 3)
    def __unicode__(self):
        return self.object_name



