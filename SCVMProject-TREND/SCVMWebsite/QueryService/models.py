from django.db import models


# Create your models here.
class BDSA(models.Model):
	cve_id = models.CharField('CVE-ID', max_length=50, primary_key=True)
	bdsa_id = models.CharField('BDSA-ID', max_length=50, unique=True)
	title = models.TextField('Title',max_length=500)
	json_raw = models.TextField('json_raw')

	def __str__(self):
		return self.cve_id

