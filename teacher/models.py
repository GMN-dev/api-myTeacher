from django.db import models
from .utils import upload_image_formater
from django.urls import reverse


# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length = 100, null=False, blank=False)
    valor_hora = models.DecimalField(max_digits=9, decimal_places = 2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to=upload_image_formater, null=False, blank=False)

    class Meta:
        db_table ="Tbl_Professores"
        managed = True
    
    def __str__(self):
        return self.nome
    

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
    





class Aula(models.Model):
    nome = models.CharField(max_length = 100, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    data = models.DateTimeField( null=True, blank=True)
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, null=False, blank=False, related_name="aulas")
