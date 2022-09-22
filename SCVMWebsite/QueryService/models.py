from django.db import models

# Create your models here.
class BDSA(models.Model):
	cve_id = models.CharField('CVE-ID', max_length=50)
	bdsa_id = models.CharField('BDSA-ID', max_length=50)
	title = models.CharField('Title',max_length=500,)
	description = models.CharField('Description',max_length=500)
	technical_description = models.CharField('Technical Description',max_length=500)
	solution = models.CharField('Solution',max_length=500,)
	patch_links = models.TextField('Patch Links',max_length=500)
	mitigation = models.CharField('Mitigation',max_length=500)
	vul_function = models.CharField('Vulnerable Function', max_length=500)

	def __str__(self):
		return self.cve_id