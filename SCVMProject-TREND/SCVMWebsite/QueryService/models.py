from django.db import models
from django.utils import timezone

# Create your models here.
class BDSA(models.Model):
	cve_id = models.CharField('CVE-ID', max_length=50)
	bdsa_id = models.CharField('BDSA-ID', max_length=50, primary_key=True)
	title = models.TextField('Title',max_length=500)
	added_date = models.DateTimeField(default=timezone.now)
	json_file = models.FileField(blank=True, null=True, upload_to="json_files")

	def __str__(self):
		return self.cve_id

