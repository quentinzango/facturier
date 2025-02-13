from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

    """
    Name: Customer model definition
    """

    name = models.CharField(max_length=132)

    email = models.EmailField()

    phone = models.CharField(max_length=132)

    age = models.CharField(max_length=12)

    created_date = models.DateTimeField(auto_now_add=True)

    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)



class Meta:
    verbose_name = "Customer"
    verbose_name_plural = "Costomers"

    def __str__(self):
        return self.name

class Invoice(models.Model):
        """
        Name: Invoice model definition
        Description:
        author:quentinzango470@gmail.com
        """

        INVOICE_TYPE = (
            ('F', 'FACTURE'),
            ('P', 'PROFORMA FACTURE'),
        )

        customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

        saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

        invoice_date_time = models.DateTimeField(auto_now_add=True)

        total = models.DecimalField(max_digits=1000000, decimal_places=2)

        last_updated_date = models.DateField(null=True, blank=True)

        paid = models.BooleanField(default=False)

        invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)

        comments = models.CharField(null=True, max_length=1000, blank=True)



        class Meta:
            verbose_name = 'Invoice'
            verbose_name_plural = 'Invoices'

        def __str__(self):
            return f"{self.customer.name}_{self.invoice_date_time}"    
        @property
        def get_total(self):
            articles = self.article_set.all()
            total = sum(article.get_total for article in articles)

class Article(models.Model):
     """
     Name: Article model definition
     Description:
     Author: quentinzango@gmail.com
     """

     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

     name = models.CharField(max_length=32)

     quantity = models.IntegerField()

     unit_price =  models.DecimalField(max_digits=1000, decimal_places=2)

     total = models.DecimalField(max_digits=1000, decimal_places=2)

     class Meta:
          verbose_name = 'Article'
          verbose_name_plural = 'Articles'

     @property
     def get_total(self):
         total = self.quantity * self.unit_price

    

