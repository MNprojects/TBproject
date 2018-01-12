from django.db import models

""" ------------------------------------------------------------------------------------------------------
    My code
------------------------------------------------------------------------------------------------------ """

class Photo(models.Model):
    name = models.CharField(max_length=200)
    dateTaken = models.DateTimeField('Date taken')
    caption =  models.CharField(max_length=200, help_text = "Enter a caption for the photo")
    photo = models.ImageField(upload_to='photos/', default = '')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('Photo-detail', args=[str(self.id)])