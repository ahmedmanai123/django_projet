from cProfile import Profile
from urllib import request
from ArtyProd import settings
from django.contrib.auth.decorators import login_required
from ArtyProd.settings import EMAIL_HOST_USER
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .models import  Detail, Personnel, Projet, Service,User,Profile
from .models import Product 
from django.core.mail import send_mail, BadHeaderError
from django.http import Http404, HttpResponse
from .forms import CustomUserCreationForm, UserRegistrationForm,UserCreationForm, projetform
from .models import Portfolio
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
def index(request):
          return render( request,'/projet/base.html')

def portfolio(request):
  projects = Projet.objects.all()
  return render(request, 'projet/portfolio.html', {'projects': projects})
   
  
#def homepage(request):
	#product = Product.objects.all() #queryset containing all products we just created
	#return render(request=request, template_name="projet/portfolio.html", context={'product':product})
def index1(request):
         return render( request,'Interface/index.html' )

    


def portfolio_view(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'Interface/portfolio.html', {'portfolios': portfolios})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'Interface/profile.html', {'profile': profile})

def services_view(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'Interface/services.html', context)

def EquipeView(request):
    equipes = Personnel.objects.all()
    return render(request, 'Interface/equipe.html', {'equipes': equipes})


def home(request):
    
    return render(request, 'Interface/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(
            subject,  
            message,  
            email,  
            [settings.DEFAULT_FROM_EMAIL],  
            fail_silently=False, 
        )

        context = {
            'message': f"Merci {name} ! Votre message a bien été envoyé.",
        }
        return render(request, 'Interface/contact.html', context)

    else:
        return render(request, 'Interface/contact.html')


def portfolio_detail(request,id):
  portfolio_detail=Portfolio.objects.get(id=id)
  context={'portfolio_detail':portfolio_detail}
  return render(request, 'Interface/portfolio_details.html', context)



def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def LogoutView(request):
     logout(request)
     return redirect ('index1')
def LoginView(request):
     if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password= password)
            if user is not None:
                login(request, user)
                return redirect('index1')
            else:
                error_message = 'Invalid email or password'
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_msg = 'Invalid form submission'
            return render(request, 'registration/login.html', {'error_msg': error_msg})
           
            
     
     return redirect (request,'registration/login.html')

def ajouter_projet(request):
    if request.method == 'POST' :
        form =projetform(request.POST,request.FILES)
        if form.is_valid():
           form.save()

    else:


        form=projetform()
        
            
            
        
    return render(request,'registration/ajoute_projet.html',{'form': form}) 

def projet (request):
    projects = Projet.objects.all()
    return render(request, 'Interface/projet_details.html', {'projects': projects})





@login_required
def project_detail(request, id):
    user_id = request.user.id
    
    project = Projet.objects.filter(user_id=user_id, id=id).first()

    if not project:
        raise Http404('Project not found')

    details = request.user.id
    context = {'project': project, 'details': details}
    return render(request, 'Interface/projet_details.html', context)


def project_details(request, project_id):
    project = get_object_or_404(Projet, id=project_id)
    return render(request, 'Interface/projet_details.html', {'project': project})