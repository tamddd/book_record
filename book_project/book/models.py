from django.db import models

CATEGORY = (('business', "ビジネス"), ('computer', "コンピュータ"),
            ('other', "その他"))

EVALUATION = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))

class BookModel(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    reports = models.TextField()
    purchase_date = models.DateField(auto_now=True)
    finished_date = models.DateField(blank=True, null=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    evaluation = models.CharField(
        max_length=1,
        choices = EVALUATION
    )

    def __str__(self):
        return self.title
