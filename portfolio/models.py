from django.db import models


class ProjectType(models.TextChoices):

        FLYER = 'flyer'
        LOGO = 'logo'
        THREE_D = '3d'
         

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True, default='')
    project_type = models.CharField(max_length=220, choices=ProjectType.choices, default=ProjectType.LOGO)

    def __str__(self):
        return self.title
