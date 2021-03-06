""" Post model module """

from django.db import models

class Post(models.Model):
    """ Representation of a post that a user can create """

    author = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    image_url = models.URLField()
    publication_date = models.DateField(auto_now_add=True, auto_now=False)
    content = models.CharField(max_length=500)
    approved = models.BooleanField(default=False)

    @property
    def is_owner(self):
        return self.__is_owner

    @is_owner.setter
    def is_owner(self, value):
        self.__is_owner = value
