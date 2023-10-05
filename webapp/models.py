from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(max_length=100)
    project_subject = models.CharField(max_length= 350)
    project_description = models.CharField(max_length=700)
    client_firstname = models.CharField(max_length= 100)
    client_lastname = models.CharField(max_length= 100)
    client_contact = models.CharField(max_length=100)
    project_link = models.URLField(max_length=500)
    
    def __str__(self):
        return self.client_firstname+"  "+self.client_lastname
