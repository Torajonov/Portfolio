from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Emaili', max_length=200)
	subject = models.CharField('subject', max_length=50)
	message = models.CharField('Xabari', max_length=250)

	class Meta:
		verbose_name = 'contact'
		verbose_name_plural = 'Contactlar'

	def __str__(self):
		return f"{self.name}"