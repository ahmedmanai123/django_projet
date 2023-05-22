from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.db import models


from django.dispatch import receiver

class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    personnel = models.ManyToManyField('Personnel', related_name='equipes')
    def __str__(self):
        return self.nom

    
class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    ficher_CV = models.ImageField(upload_to='cv/')
    ficher_photo = models.ImageField(upload_to='images/personnel')
    lien_linkidin = models.URLField(max_length=200)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, related_name='equipe_personnel')
    def __str__(self):
        return self.nom



class Service(models.Model):
    
    type = models.CharField(max_length=100)
    nom = models.CharField(max_length=100, default='')
    description = models.TextField()
    def __str__(self):
        return self.nom
        
class Projet(models.Model):
    libellai = models.CharField(max_length=100)
    description = models.TextField()
    services = models.ManyToManyField(Service)
    date_debut = models.DateField()
    date_fin = models.DateField() 
    pdf_projet=models.FileField(upload_to='img')
    acheve = models.BooleanField(default=False)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    def __str__(self):
        return self.libellai
                
    

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	product_type = models.CharField(max_length=25)
	product_description = models.TextField()
	affiliate_url = models.SlugField(blank=True, null=True)
	product_image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.product_name
class Detail(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='details')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='fichiers/')

    def __str__(self):
        return f"{self.service.type} - {self.projet.libellai}"
    
    fichier = models.FileField(upload_to='fichiers/')
class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    
class Portfolio(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/portfolio')
    temoignages = models.TextField()
 
class Contact (models.Model):
     name=models.CharField(max_length=100)
     email =models.EmailField()
     sujet=models.CharField(max_length=200)
     messaage=models.TextField(max_length=500)
     def __str__(self) :
          return self.name
                   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)
    def get_user_projects(self):
        return Projet.objects.filter(user=self.user)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  
       