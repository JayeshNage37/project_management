from django.db import models

# CLASS NAME:Product
# DESCRIPTION: This model stores product details.
# AUTHOR: Jayesh Nage
# Date: 01/05/2021
class Project(models.Model):
    name = models.CharField(max_length =256 , null=True)
    description = models.CharField(max_length =256 , null=True)
    duration =models.IntegerField()
    project_image = models.ImageField(null=True)
    class Meta():
        db_table = 'projects'

# CLASS NAME:Product
# DESCRIPTION: This model stores product details.
# AUTHOR: Jayesh Nage
# Date: 02/05/2021
class Task(models.Model):
    name = models.CharField(max_length =256 , null=True)
    description = models.CharField(max_length =256 , null=True)
    start_date =models.DateField()
    end_date =models.DateField()
    project_id = models.IntegerField()
    class Meta():
        db_table = 'tasks'