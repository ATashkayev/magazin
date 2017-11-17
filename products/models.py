from django.db import models

class ProductGroup(models.Model):
	name = models.CharField(verbose_name=u'Группы товара', max_length=60)

	def __str__(self):
		return '%s : %s' % (self.id, self.name)

class Products(models.Model):
	name = models.CharField(verbose_name=u'Представление товара, наименование',max_length=60)
	description = models.CharField(verbose_name=u'Описание товара',max_length=600, blank=True)
	number = models.IntegerField(verbose_name=u'Остаток товара', default=0)
	price = models.DecimalField(verbose_name=u'Цена товара', max_digits=12, decimal_places=2, default=0, blank=True)
	discount = models.DecimalField(verbose_name=u'Скидка', max_digits=2, decimal_places=0, default=0, blank=True)
	min_price = models.DecimalField(verbose_name=u'Закупочная цена товара', max_digits=12, decimal_places=2, default=0, blank=True)
	first_foto = models.ImageField(upload_to='foto/', height_field=None, width_field=None, max_length=900, blank=True)
	is_active = models.BooleanField(default=True)
	group = models.ForeignKey(ProductGroup, blank=True, null=True, default=None)
	size = models.CharField(verbose_name=u'Остатки размеров',max_length=250, blank=True, null=True, default=None)

	def __str__(self):
		return '%s : %s' % (self.name, self.price)

class Spisok_foto(models.Model):
	product = models.ForeignKey(Products, blank=True, null=True, default=None)
	foto = models.ImageField(upload_to='foto/', height_field=None, width_field=None, max_length=900)
	
	def __str__(self):
		return '%s' % self.id
	
	class Meta:
		verbose_name = 'Фотографии товаров'
		verbose_name_plural = 'Фотографии товаров'