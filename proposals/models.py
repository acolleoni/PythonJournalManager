from django.db import models

#BaseModel is needed just in order to be able to use the IDE PyCharm Community
class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class CallForPapers(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "call for papers"

class Proposer(BaseModel):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Proposal(BaseModel):
    title = models.CharField(max_length=64)
    proposer = models.ManyToManyField(Proposer, related_name="articles")
    call_for_papers = models.ForeignKey(CallForPapers, on_delete=models.CASCADE, related_name="articles")
    abstract = models.TextField()
    pdf_url = models.CharField(max_length=64)
    states=(
        (0, 'New'),
        (1, 'In Review'),
        (2, 'Accepted'),
        (3, 'Refused')
    )
    state = models.IntegerField(choices=states)
    def __str__(self):
        return self.title

class Review(BaseModel):
    reviewer_name = models.CharField(max_length=64)
    reviewer_surname = models.CharField(max_length=64)
    reviewer_email = models.CharField(max_length=64)
    pdf_url = models.CharField(max_length=64)
    states=(
        (0, 'Initial'),
        (1, 'Accepted'),
        (2, 'Minor Review'),
        (3, 'Major Review'),
        (4, 'Refused')
    )
    state = models.IntegerField(choices=states)
    def __str__(self):
        return self.reviewer_name
    proposal=models.ManyToManyField(Proposal, related_name="articles")
