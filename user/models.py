  
from django.db      import models

from .validators    import phone_number_validation_function, password_validation_function

class User(models.Model): 
    name         = models.CharField(max_length = 16)
    birthdate    = models.DateField(max_length = 16)
    identifier   = models.CharField(max_length = 64, unique = True)
    password     = models.CharField(max_length = 256, validators = [password_validation_function])
    gender       = models.CharField(max_length = 8)
    phone_number = models.CharField(max_length = 17, validators = [phone_number_validation_function], unique = True)
    kakao_user   = models.CharField(max_length = 64, null = True)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)

    class Meta: 
        db_table = "users"