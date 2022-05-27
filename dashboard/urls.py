from django.urls import path
from django.views import View
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name= 'dashboard'),
    path('service_orders', views.orders, name='orders' ),
    path('delete/<int:id>', views.deleteOrder, name='delete'),
    path('message/', views.messageSite, name='siteMessages'),
    # ---- blog ---
    path('blog/', views.menagePosts, name='listPost'),
    path('blog/new/post', views.writePost, name='writePost'),
    path('blog/new/create/', views.createPost, name='createPost'),
    path('blog/edit/post/<int:id>/', views.editPost, name='editPost'),
    path('blog/delete/post/<slug:slug>/', views.deletePost, name='deletePost'),
    # ---- portfolio ----
    path('portfolio/', views.managePortifolio, name='managePortifolio'),
    path('portfolio/new/', views.addInPortifolio, name='addInPortifolio'),
    path('portfolio/edit/<int:id>/', views.editPortfolioItem, name='editPortfolio'),
    path('portfolio/delete/<int:id>/', views.delete_from_Portifolio, name='delete_from_portifolio'),
    # ---- Widget Slider ----
    path('slider/', views.manageSlider, name='manageSlider'),
    path('slide/new/', views.addSlide, name='addSlide'),
    path('slide/edit/<int:id>/', views.editSlide, name='editSlide'),
    path('slide/delete/<int:id>/', views.deleteSlide, name='deleteSlide'),
    # ---- widget our clients ----
    path('nossosclientes/', views.manageOursClients, name='manageOursClients'),
    path('nossosclientes/new/', views.addOurClient, name='addOurClient' ),
    path('nossoscliente/edit/<int:id>/', views.editOurClient, name='editOurClient'),
    path('nossosclientes/delete/<int:id>/', views.deleteOurClient, name='deleteOurClient'),
    # ---- Links Uteis ----
    path('linksuteis/', views.manageLinks, name='manageLinks'),
    path('linksuteis/new/', views.addLink, name='newLink'),
    path('linksuteis/edit/<int:id>/', views.editLink, name='editLink'),
    path('linksuteis/delete/<int:id>/', views.deleteLink, name='deleteLink'),
    # ---- logout ---
    path('logout/', views.logout_view, name='logout'),
    path('meuperfil/', views.managePerfil, name='managePerfil'),
]