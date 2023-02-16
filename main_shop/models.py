from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from numpy import double, maximum, product
from django.core.validators import MinValueValidator, MaxValueValidator
from soupsieve import select
from tomlkit import datetime, value
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.
class Categories(models.Model):
    Category_name = models.CharField("Назва категорії",max_length=50)
    Category_desc= models.TextField("Короткий опис товарів у категорії",max_length=50)
    def __str__(self):
        return self.Category_name
    class Meta:
        verbose_name="Категорія"
        verbose_name_plural="Категорії"

class Orders(models.Model):
    user_id=models.CharField("Username",max_length=200,default=0)
    product_id=models.CharField("ID продукту",max_length=200,default=0)
    product_name=models.CharField("Назва продукту",max_length=200,default=0)
    product_png=models.ImageField(upload_to="media\img\%Y\%m\%d",default=0,null=True,blank=True)
    num_of_products=models.DecimalField("кількість товару",max_digits=15,decimal_places=0,default=0)
    product_final_price=models.DecimalField("Ціна замовлення",max_digits=8,decimal_places=2,default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    def get_final_price(self):
        return round(self.num_of_products)
    def __str__(self):
        return str(self.id)
class Products(models.Model):
    
    product_name = models.CharField("Назва товару",max_length=150)
    Category_name = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_description=models.CharField("опис товару",max_length=350)
    number_of_prouct=models.DecimalField("кількість товару",max_digits=15,decimal_places=2,default=0)
    product_png=models.ImageField(upload_to="media\img\%Y\%m\%d",default=0,null=True,blank=True)
    product_price_initial=models.DecimalField("Початкова ціна",max_digits=15,decimal_places=2)
    product_discount=models.DecimalField("Відсоток знижки",max_digits=4,decimal_places=2,default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    Date_of_get=models.DateField("Дата отримання",auto_now=True)
    unit_of_measure = models.CharField("Одиниці вимірювання",max_length=150,default='кг')
    def __str__(self):
         return self.product_name
    def get_way(self):
        return self.product_png
    def get_num(self):
        return round(self.number_of_prouct,0)
    def get_final_price(self):
        return round(self.product_price_initial - self.product_price_initial/100 * self.product_discount,2)


class Order_In_Wrork(models.Model):
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        
        order_info=models.CharField("Дані про замовлення",max_length=2000000,default=0)
        user_id=models.CharField("Username",max_length=2000,default=0)
        ord_name=models.CharField("Ім'я отримувача",max_length=2000,default=0)
        ord_surname=models.CharField("Прізвище отримувача",max_length=2000,default=0)  
        phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,default=0) # Validators should be a list
        adress =models.CharField("Адреса користувача",max_length=2000,default=0)
        additional_info=models.CharField("Додаткова інформація",max_length=2000,default=0)
        def __str__(self):
            return self.adress