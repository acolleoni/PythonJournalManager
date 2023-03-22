from django.db import models

#Il basemodel serve a far funzionare pyCharm Community
class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Issue(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField()
    img_url = models.CharField(null=True, blank=True, max_length=64)
    pdf_url = models.CharField(max_length=64)
    def __str__(self):
        return self.title

class Article(BaseModel):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="articles")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="articles")
    abstract = models.TextField()
    img_url = models.CharField(null=True, blank=True, max_length=64)
    pdf_url = models.CharField(max_length=64)
    def __str__(self):
        return self.title

