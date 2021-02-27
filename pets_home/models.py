from django.db import models
from django.core import validators

class TypeOfAnimal(models.Model):
	animal_type = models.CharField(max_length=50)

	def __str__(self):
		return self.animal_type


class Pets(models.Model):
	name = models.CharField(max_length=50, verbose_name="Прозвище")
	breed = models.CharField(max_length=50, verbose_name="Порода")
	description = models.TextField()
	age = models.SmallIntegerField(verbose_name="Возраст", validators=[validators.MaxValueValidator(50)])
	date_of_receipt = models.DateTimeField(auto_now=True, verbose_name="Дата прихода")
	type_of_animal = models.ForeignKey(TypeOfAnimal, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photo', blank=True)

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url

	def __str__(self):
		return self.name


# Create your models here.
