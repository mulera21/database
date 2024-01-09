from django.db import models
 
# declare a new model with a name "Geek"
class Geek(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.FileField(upload_to="project_images/", blank=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
   
   
   
   


   