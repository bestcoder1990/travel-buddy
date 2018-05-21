from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['name']) < 3:
            result['errors'].append("Must enter first name of at least two characters")
        if len(postData['username']) < 3:
            result['errors'].append("Must enter username of at least two characters")
        if User.objects.filter(username = postData['username']).count() > 0:
            result['errors'].append("Username address is already registered")
        if len(postData['password']) < 8:
            result['errors'].append("Password must be at least eight characters")
        if postData['password'] != postData['confirm']:
            result['errors'].append("Password confirmation does not match")
        if len(result['errors']) < 1:
            result['status'] = True
            result['user_id'] = User.objects.create(
                name=postData['name'],
                username=postData['username'],
                hashpw=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())).id
            print("no errors")
        print("errors")
        return result

    def log_validator(self, postData):
        existing_user = User.objects.filter(username=postData['username'])
        result = {
            'status' : False,
            'errors' : []
        }
        if existing_user.count() == 0:
            result['errors'].append("Invalid login information")
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_user[0].hashpw.encode()):
                result['status'] = True
                result['user_id'] = existing_user[0].id
            else:
                result['errors'].append("Invalid login information")
        return result

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()