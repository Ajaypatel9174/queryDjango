from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    class Meta:
        db_table = "Student"   

    def __str__(self):
        return self.name+"     "+self.email+"     "+self.city+"     "
    

    
    




    

    

    


