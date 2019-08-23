from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name needs to be more than 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name needs to be more than 2 characters'
        if len(postData['email']) <= 0:
            errors['email_required'] = 'Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email_invalid'] = 'Enter valid email address'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be 8 haracters or longer'
        elif (postData['password']) != postData['confirm_password']:
            errors['confirm_password'] = 'password does not match'
        return errors
    
    def login_validator(self, postData):
        errors = {}
        email_to_check = User.objects.filter(email=postData['login_email'])
        if len(postData['login_password']) < 8:
            errors['login_password'] = 'Password must be 8 haracters or longer'
        if len(postData['login_email']) <= 0:
            errors['email_required'] = 'Email is required'
        elif not EMAIL_REGEX.match(postData['login_email']):
            errors['email_invalid'] = 'Enter valid email address'
        elif len(email_to_check) == 0:
            errors['credentials'] = 'Invalid credentials. Try again.'
        elif len(email_to_check) == 1:
            user_logging_in = User.objects.get(email=postData['login_email'])
            if user_logging_in.password != postData['login_password']:
                errors['credentials'] = 'Invalid credentials. Try again.'
        return errors
      
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)
    objects = UserManager()

class wall_post(models.Model):
    wall_post = models.TextField()
    user = models.ForeignKey(User, related_name='wall_post')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    text = models.CharField(max_length=200, default='')
    creator = models.ForeignKey(User, related_name='user_Comment', default=1)
    commented_wall_post = models.ForeignKey(wall_post, related_name='wall_post_Comment', default=1)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


# wall_post.wall_post_Comment # this will show me my children comments


# comment.commented_wall_post #this will show me my parent wall_post