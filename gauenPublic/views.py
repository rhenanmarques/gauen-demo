
from blog.models import Post
from dashboard.models import OursClients, Portfolio, Slider
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from utils.gauenPublic.djangoViews import ConstructResp, CheckCookies
from utils.gauenPublic.simulador import *

from gauenPublic.models import Price, UsefulLinks

from .forms import *


# Create your views here.
    

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-id')[:3]
    slides = Slider.objects.filter(is_published=True)
    clients = OursClients.objects.filter(is_activate=True).order_by('-id')
    context = {
        'posts': posts,
        'slides': slides,
        'clients': clients,
    }
    
    CheckCookies(request, context)

    response = render(request, 'gauenPublic/pages/home.html', context)

    return response

def viewCookies(request):
    gauenCookie = {'key':'GauenCookie', 'value': 'True'}#criar um dicionario para cada cookie
    response = JsonResponse({"foo":"bar"})
    if request.method == 'GET':      
        response.set_cookie(gauenCookie['key'], gauenCookie['value'])
        #set todos os cookies
        return response
    
    if request.method == 'POST':
        print("foi o post")
        """allowed = []
        #pegar o valor de todos os campos e os que forem verdadeiros apped allwed
        for cookie in allowed:
            response.set_cookie(cookie['key'], cookie['value'])"""
        return response



def contact(request):
    form = ContactoForm()
    context = {'form':form}

    CheckCookies(request, context)

    return render(request, 'gauenPublic/pages/contact.html', context)

def createMessage(request):

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Obrigada. O carteiro está a caminho :)")
            return redirect(reverse('gauenPublic:contact'))
        else:
            messages.error(request, "Desculpe, não sei o que aconteceu. Tente depois :(")
            return render(request, 'gauenPublic/pages/contact.html', {'form':form})


def about(request):
    context = {}
    CheckCookies(request, context)
    return render(request, 'gauenPublic/pages/about.html', context)


def ourService(request):
    context = {}
    CheckCookies(request, context)
    return render(request, 'gauenPublic/pages/our_services.html', context)

def usefulLinks(request):
    links = UsefulLinks.objects.all()
    #get_list_or_404(UsefulLinks)
    context = {'links': links}
    return render(request, 'gauenPublic/pages/usefuLinks.html', context)


def portfolio(request):
    portfolio = Portfolio.objects.filter(is_Public=True).order_by('-id')
    clients = OursClients.objects.filter(is_activate=True).order_by('-id')

    context = {
        'clients': clients,
        'portfolio':portfolio
    }
    CheckCookies(request, context)
    return render(request, 'gauenPublic/pages/portfolio.html', context)

def simulator(request):
    util = SimulatorForm()
    cargaIncendio = Ambiente()
    materiais = Materiais()

    context ={
        'form': util,
        'cargaIncendio': cargaIncendio,
        'materiais': materiais
    }
    CheckCookies(request, context)
    return render(request, 'gauenPublic/pages/simulator.html', context)


def result(request):

    if request.method == "POST":
        ut = request.POST.get('utilizacao_Tipo', None)
        altura = request.POST.get('altura', None)
        efetivo = request.POST.get('efetivo_Total', None)
        subsolo = request.POST.get('subsolo', None)
        areaBruta = request.POST.get('area_Bruta', None)
        arLivre = request.POST.get('ar_Livre', None)
        localRiscoD = request.POST.get('local_Risco_D', None)
        efetivoLocalD = request.POST.get('efetivo_Local_D', None)
        localRiscoE = request.POST.get('local_Risco_E', None)
        efetivoLocalE = request.POST.get('efetivo_Local_E', None)

        
        if ut == "1":
            categoria = habitacionais(float(altura), int(subsolo))
            
            resp = ConstructResp('Habitacionais', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']

            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "2":

            if arLivre == 'no':                
                categoria = estacionamentos(float(altura), int(subsolo), float(areaBruta))
            else:
                categoria = estacionamentos(0, 0, float(areaBruta), True)

            resp = ConstructResp('Estacionamentos', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']

            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "3":

            categoria = administrativos(float(altura), int(efetivo))
            
            resp = ConstructResp('Administrativos', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']

            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "4":


            if localRiscoD == 'no':
                categoria = escolares_Hospitalares(float(altura), int(efetivo))
            else:
                categoria = escolares_Hospitalares(float(altura), int(efetivo), True, False, int(efetivoLocalD))

            resp = ConstructResp('Escolares', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "5":


            if localRiscoD == 'no':
                categoria = escolares_Hospitalares(float(altura), int(efetivo))
            else:
                categoria = escolares_Hospitalares(float(altura), int(efetivo), True, False, int(efetivoLocalD))

            resp = ConstructResp('Hospitalares e Lares de Idosos', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "6":

            if arLivre == 'no':
                categoria = espetaculos_Desportivos(float(altura), int(subsolo), int(efetivo))
            else:
                categoria = espetaculos_Desportivos(0, 0, int(efetivo), True)

            resp = ConstructResp('Espectáculos e Reuniões Públicas', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "7":

            if localRiscoE == 'no':
                categoria = restauracao_Hotelaria(float(altura), int(efetivo))
            else:
                categoria = restauracao_Hotelaria(float(altura), int(efetivo), efetivoLocalE)

            resp = ConstructResp('Hoteleiros e Restauração', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "8":
            categoria = comerciais(float(altura), int(subsolo), int(efetivo))

            resp = ConstructResp('Comerciais e Gares de Transportes', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "9":
            if arLivre == 'no':
                categoria = espetaculos_Desportivos(float(altura), int(subsolo), int(efetivo))
            else:
                categoria = espetaculos_Desportivos(0, 0, int(efetivo), True)

            resp = ConstructResp('Desportivos e de Lazer', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "10":
            if arLivre == 'no':
                categoria = museus_GaleriasArte(float(altura), int(subsolo), int(efetivo))
            else:
                categoria = museus_GaleriasArte(0, 0, int(efetivo), True)

            resp = ConstructResp('Museus e Galerias de Arte', categoria)
            request.session['data_simulation'] = resp.resposta()
            context = request.session['data_simulation']
           
            return render(request, 'gauenPublic/pages/result.html', context)

        elif ut == "11":
            #terminar o formulario no js
            pass
        elif ut == "12":
            #terminar o formulario no js
            pass
    
    messages.warning(request, "Ops! Parece que você está com pressa. Siga as instruções do simulador para descobrir a categoria de risco do seu edifício")
    return redirect("gauenPublic:simulator") 


def requestService(request):
    if 'data_simulation' not in request.session:
        messages.warning(request, "Ops! Parece que você está com pressa. Para que possamos atender-lo melhor, antes de criar uma solicitação siga as instruções do simulador.")
        return redirect("gauenPublic:simulator")    

    formRequest = MapForm()
    context = {
        'form': formRequest,
        'temp': request.session.get('data_simulation', None)
    }
    
    CheckCookies(request, context)

    if request.method == "POST":
        formRequest = MapForm(request.POST)
        if formRequest.is_valid():
            data = formRequest.save(commit=False)
            data.utilizacao_Tipo = request.session.get('data_simulation')['id_UT']
            data.categoria = request.session.get('data_simulation')['cat']
            data.price = request.session.get('data_simulation')['price']
            data.save()
            context['successful_submit'] = True
            del request.session['data_simulation']
            return render(request, 'gauenPublic/pages/request_service.html', context)
        
        context = {
            'form': formRequest,
            'temp': request.session.get('data_simulation', None)
        }

        messages.error(request, "Corrija os erros para continuar")
        return render(request, 'gauenPublic/pages/request_service.html', context)
            
        
    return render(request, 'gauenPublic/pages/request_service.html', context)

def sucess(request):
    return render(request, 'gauenPublic/pages/sucess.html')


    