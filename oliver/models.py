import hashlib
from django.db import models

# Create your models here.

class Account(models.Model):
	accountid=models.IntegerField()
	name=models.ChardField(max_length=200)
	email=models.EmailField()
	password=models.CharField(max_length=200)





    def check_password(self, password):
        if self.password(password) == self.password:
            return True
        return False

    class Meta:
        db_table = "restapp"
	
