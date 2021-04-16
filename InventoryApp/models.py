from django.db import models

# Create your models here.
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    send_to_manager = models.BooleanField(default=False,db_index=True)# sent only when element is issued

    issued=models.BooleanField(default=False,db_index=True)# Not Initially  issued.
    def __str__(self):
        return self.name



class AccessRequest(models.Model):

    Request_States=[
        ('Not Sent','Not Sent'),
        ('Sent','Sent'),
        ('Accepted','Accepted'),
        ('Denied','Denied'),
    ]

    access_request=models.CharField(max_length=10,choices=Request_States,db_index=True)# Request initailly not sent
    issued_element= models.ForeignKey(Equipment,on_delete=models.CASCADE)
    user_choices=[
        ('Employee','Employee'),
        ('Manager','Manager')
    ]
    user_type=models.CharField(max_length=10,choices=user_choices)

    def __str__(self):
        return f" Request from {user_type} -> {self.access_request} "
    
