from __future__ import unicode_literals
from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData, id=0, update=False):
        errors = {}
        # If we're doing an update, get an instance of the current user
        if update:
            user = User.objects.get(id=id)
        
        if len(postData['fName']) < 1:
            errors['fName'] = "Please enter your first name"
        elif len(postData['fName']) < 3:
            errors['fName'] = "First name should be at least 3 characters"
        elif not postData['fName'].isalpha():
            errors['fName'] = "First name should only only contain alphabetical characters"

        if len(postData['lName']) < 1:
            errors['lName'] = "Please enter your last name"
        elif len(postData['lName']) < 3:
            errors['lName'] = "Last name should be at least 3 characters"
        elif not postData['fName'].isalpha():
            errors['lName'] = "Last name should only only contain alphabetical characters"

        if 'email' in postData:
            if len(postData['email']) < 1:
                errors['email'] = "Please enter your email address"
            else:
                evalidator = EmailValidator()
                try:
                    evalidator(postData['email'])
                except:
                    # print("This is my issues that i keep having:", issue)
                    errors['email'] = "Please enter a valid email address"
            
            if 'email' not in errors:
                try:
                    if User.objects.get(email=postData['email']):
                        if update:
                            if postData['email'] != user.email:
                                errors['email'] = "Email address already taken"
                        else:
                            errors['email'] = "Email address already taken"
                except:
                    print("No query")

        
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = UserManager()