from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
class Yonalish(models.Model):
    nom = models.CharField(max_length=255,choices=(('Iqtisod','Iqtisod'),('Moliya','Moliya'),('IT','IT')))
    aktiv = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name ='Yonalish'
        verbose_name_plural ='Yonalishlar'

class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.SET_NULL,null=True)
    asosiy = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name ='Fan'
        verbose_name_plural ='Fanlar'

class Ustoz(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10,choices=(('Erkak','Erkak'),('Ayol','Ayol')))
    yosh = models.PositiveSmallIntegerField(validators=[MinValueValidator(25),MaxValueValidator(60)],default=25)
    daraja = models.CharField(max_length=50,choices=(('Bakalavr','Bakalavr'),('Magistr','Magistr'),('PHD','PHD')))
    fan = models.ForeignKey(Fan,on_delete=models.SET_NULL,null=True)
    oilali=models.BooleanField(default=False)
    def __str__(self):
        return self.ism

    class Meta:
        verbose_name ='Ustoz'
        verbose_name_plural ='Ustozlar'
