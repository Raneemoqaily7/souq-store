from django.db import models
from django.utils.translation import gettext_lazy as _


class Product (models.Model):
    PRDName = models.CharField(max_length = 100 , verbose_name = _("Product Name"))
    PRDDesc = models.TextField (verbose_name = ("Description"))
    PRDPrice = models.DecimalField(max_digits = 6 , decimal_places= 3  , verbose_name = _("Price"))
    PRDCost =models.DecimalField(max_digits = 6 , decimal_places= 3 , verbose_name = _("Cost"))
    PRDCreated =models.DateTimeField (verbose_name = _("created at"))


    def __str__(self):
        return self.PRDName






class ProductImage(models.Model):
    PRDIMProduct=models.ForeignKey(Product,on_delete =models.CASCADE, verbose_name = _("product"))
    PRDIMImage =models.ImageField (upload_to ='products/' , verbose_name =_("Image")) 

    def __str__(self):
        return str(self.PRDIMProduct)
 



class Category (models.Model):
    CATName = models.CharField (max_length = 50 ,verbose_name = _("category"))
    CATParent = models.ForeignKey ('self' ,on_delete = models.CASCADE ,limit_choices_to={'CATParent__isnull': True},blank=True,
    null=True ,verbose_name = ("Main category"))
    CATImage= models.ImageField (upload_to = 'category/')
    CATDesc = models.TextField ()


    def __str__ (self):
        return self.CATName



class Alternative(models.Model):
    ALTProd = models.ForeignKey (Product,on_delete =models.CASCADE,related_name ='ALT_product' ,verbose_name = _("product") )
    ALTProducts =models.ManyToManyField(Product ,related_name ='Alternative_products' , verbose_name = _("Alternative products") )

    def __str__(self):
        return str(self.ALTProd)

class Accsesory(models.Model):
    ACCSProd = models.ForeignKey (Product,on_delete =models.CASCADE, verbose_name = _("product") ,related_name ='ACC_product')
    ACCSProducts =models.ManyToManyField(Product ,related_name ='Accsesories' , verbose_name = _("Accsesories") )

    def __str__(self):
        return str(self.ACCSProd)


    