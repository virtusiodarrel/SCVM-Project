from django.db import models

# Create your models here.
class BDSA(models.Model):
	cve_id = models.CharField('CVE-ID', max_length=50, unique=True)
	bdsa_id = models.CharField('BDSA-ID', max_length=50)
	title = models.TextField('Title',max_length=500)
	description = models.TextField('Description',max_length=500)
	technical_description = models.TextField('Technical Description',max_length=500,blank=True)
	solution = models.TextField('Solution',max_length=500,blank=True)
	patch_links = models.TextField('Patch Links',max_length=500,blank=True)
	mitigation = models.CharField('Mitigation',max_length=500,blank=True)
	vul_function = models.TextField('Vulnerable Function', max_length=500,blank=True)

	def __str__(self):
		return self.cve_id
