from django.db import models

class UserManager(models.Manager):
    def validator(self, post_data):
        print('post_data: ', post_data)
        errors = {}

        if len(post_data['name']) < 2:
            errors["name"] = "your first name is too short"
        if len(post_data['alias']) < 2:
            errors["alias"] = "your last name is too short"
        if len(post_data['email']) < 5:
            errors["email"] = "your email is too short"
        if len(post_data['password']) < 8:
            errors["password"] = "your password is too short"
        if (post_data['password'] != post_data['password_confirm']):
            errors['password_confirm'] = 'your password doesn\'t match'
        return errors

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    user = models.ForeignKey('Users', related_name="review")
    book = models.ForeignKey('Books', related_name="review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    # review
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Authors', related_name="books")
    # review 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


