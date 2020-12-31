from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name= models.CharField(max_length= 100)
    des= models.TextField()
    img= models.ImageField(upload_to= 'menu_img/')
    price= models.DecimalField(max_digits= 5, decimal_places= 2)
    category= models.ManyToManyField('Category', related_name= 'item')

    def __str__(self):
        return self.name

class Category(models.Model):
    name= models.CharField(max_length= 100)
    parent= models.ForeignKey('self', related_name= 'children', null= True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    created_on= models.DateTimeField(auto_now_add= True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    items= models.ManyToManyField('MenuItem',related_name= 'order', blank= True, null= True)
    name= models.CharField(max_length= 50, blank= True)
    email= models.CharField(max_length= 50, blank= True)
    street = models.CharField(max_length= 50, blank= True)
    city= models.CharField(max_length= 50, blank= True)
    state= models.CharField(max_length= 15, blank= True)
    zip_code= models.IntegerField(blank= True, null= True)
    is_paid= models.BooleanField(default = False)
    is_shipped = models.BooleanField(default = False)

    def __str__(self):
        return f'order: {self.created_on.strftime("%b %d %I: %M %p")}'