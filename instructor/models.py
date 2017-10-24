from django.db import models

# Create your models here.

class Spisok(models.Model):
	name = models.CharField(max_length=120)
	def __str__(self):
		return self.name

class Instructors(models.Model):
	name = models.CharField(max_length=60)
	surname = models.CharField(max_length=60)
	data_birth = models.DateField(verbose_name=u'Када радилси?',null=True, blank=True)
	course = models.CharField(max_length=60)
	who_i_am_s = models.ManyToManyField(Spisok)

	def __str__(self):
		return self.name

