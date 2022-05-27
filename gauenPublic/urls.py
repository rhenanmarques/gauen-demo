from django.urls import path
from . import views

app_name = 'gauenPublic'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contact, name= 'contact'),
    path('quemsomos/', views.about, name= 'about'),
    path('servicos/', views.ourService, name='services'),
    path('portfolio/', views.portfolio, name='portifolio'),
    path('simulador/', views.simulator, name='simulator'),
    path('simulador/resultado/', views.result, name='result'),
    path('simulador/solicitar_servico/', views.requestService, name='request'),
    path('sucesso/', views.sucess, name='sucess'),
    path('contacto/sendmessage', views.createMessage, name='createmessage'),
    path('links/', views.usefulLinks, name='links'),
    path('cookies/', views.viewCookies, name='cookies'),

]
