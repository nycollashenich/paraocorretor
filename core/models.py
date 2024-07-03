from django.db import models
from stdimage import StdImageField
import uuid

def get_file_path(_instance, filename): #_indicar que ele não é usado na função
    extensao = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extensao}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado em', auto_now_add=True) # na adição 
    modificado = models.DateField('Modificado em', auto_now=True) # na autualização
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True

class Corretor(Base):
    nome = models.CharField('Nome', max_length=100)
    idade = models.DecimalField('Idade', max_digits=100, decimal_places=0)
    profissao = models.CharField('Profissão', max_length=100)
    biografia = models.TextField('Biografia')
    personalidade = models.TextField('Personalidade')
    interesse = models.CharField('Interesse', max_length=100)
    missao = models.CharField('Missão', max_length=100)
    visao = models.CharField('Visão', max_length=100)
    valores = models.CharField('Valores', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Corretor'


        def __str__(self) -> str:
            return self.nome