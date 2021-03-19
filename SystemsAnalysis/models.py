from django.db import models
from django.contrib.auth.models import User

# does the standard user need to be extended? for now I don't think so

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField() # could be Char field instead , which is more space efficent, but we're running this in sqlite3 so lol who cares.
    content = models.TextField() # Text field has no max length, and even if you set one, it isn't enforced LOL
    image = models.ImageField(upload_to='images', null=True, blank=True) # I don't know how this works, but I'm adding it :)
    type = models.IntegerField()
    # should there be more, like a date ? I think django has built in dat functions
    posted = models.DateTimeField()

    def __str__(self):
        return f"{self.title}: by {self.poster}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    posted = models.DateTimeField()

class Member(models.Model): # this basically just extends the user class, allowing permissions, so that only people with a certain power level can create announcements vs blog posts vs comments
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    permission = models.IntegerField(null=True,blank=True,default = 0)
    email = models.TextField(null=True,blank=True)
    phone = models.TextField(null=True,blank=True)
    email_notif = models.BooleanField(null=True,blank=True,default = False)
    phone_notif = models.BooleanField(null=True,blank=True,default = False) # putting this extra thing in in case we need it
    image = models.ImageField(upload_to='images', null=True, blank=True) # I don't know how this works, but I'm adding it :)
    def __str__(self):
        return f"{self.id}, {self.user}, {self.permission}, {self.email}, {self.phone}, {self.phone_notif}"

class Image(models.Model): # image class, following a tutorial online :) subject to change
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

# creating the database looks like this
#`python manage.py makemigrations SystemsAnalysis`
#`python manage.py migrate `
#`python manage.py shell`

#then you can insert some data into the db with
#`from SystemsAnalysis.models import Post, Comment, Member, Image `

# and then start creating sample data.
