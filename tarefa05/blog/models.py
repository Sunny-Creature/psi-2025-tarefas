from django.db import models

# Create your models here.
class Postagem(models.Model):
    imagem = models.ImageField(upload_to="medias/",)
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=100)
    data_publicacao = models.DateField()

#class Post(models.Model):
#    imagem_post = Postagem.imagem()
#    titulo_post = Postagem.titulo()
#    texto_post = Postagem.texto()
#    data_pub_post = Postagem.data_publicacao()