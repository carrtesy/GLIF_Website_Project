from django.db import models
from users.models import Glifer
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    attached_file = models.FileField(upload_to = 'form_archive_attached_files/%Y/%m/%d/', blank = True, null = True)
    written_date = models.DateField(auto_now = True)
    writer = models.ForeignKey(Glifer, on_delete = models.CASCADE, related_name = "form_archive_writer")
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('form_archive-detail', kwargs = {'pk': self.pk})
