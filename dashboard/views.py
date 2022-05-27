from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from gauenPublic.forms import Map
from .forms import *
from gauenPublic.models import Message, UsefulLinks
from .models import *
from django.contrib import messages


# Create your views here.
@login_required(login_url='account_login', redirect_field_name='next')
def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')

@login_required(login_url='account_login', redirect_field_name='next')
def orders(request):
    ordens = Map.objects.all()
    context = {'orders': ordens}
    return render(request, 'dashboard/pages/orders.html', context)

@login_required(login_url='account_login', redirect_field_name='next')
def deleteOrder(request, id):
    order = Map.objects.get(pk=id)
    order.delete()
    return redirect(reverse('dashboard:orders'))

@login_required(login_url='account_login', redirect_field_name='next')
def messageSite(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'dashboard/pages/messageSite.html', context)

# --- Blog ---
@login_required(login_url='account_login', redirect_field_name='next')
def menagePosts(request):
    posts = Post.objects.all()
    return render(request, 'dashboard/pages/menageBlog.html', {'posts': posts})

@login_required(login_url='account_login', redirect_field_name='next')
def writePost(request):
    form = PostForm()
    return render(request, 'dashboard/pages/writePost.html', {'form': form})


@login_required(login_url='account_login', redirect_field_name='next')
def createPost(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            
            return redirect(reverse('dashboard:listPost'))
        
    return render(request, 'dashboard/pages/writePost.html', {'form': form})

@login_required(login_url='account_login', redirect_field_name='next')
def editPost(request, id):

    post = Post.objects.filter(pk=id).first()

    if not post:
        raise Http404()

    form = PostForm(
        data = request.POST or None,
        files = request.FILES or None,
        instance = post
    )
    
    if form.is_valid():
        post.save()

        messages.success(request, 'Alteração salva com sucesso!')
        return redirect(reverse('dashboard:listPost'))

    return render(
        request,
        'dashboard/pages/editPost.html',
        context={'form': form}
    )

@login_required(login_url='account_login', redirect_field_name='next')
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect(reverse('dashboard:listPost'))

# ---Portfólio---
@login_required(login_url='account_login', redirect_field_name='next')
def managePortifolio(request):
    content = Portfolio.objects.all()
    return render(request, 'dashboard/pages/managePortifolio.html', {'content':content})

@login_required(login_url='account_login', redirect_field_name='next')
def addInPortifolio(request):
    form = PortfolioForm()

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:managePortifolio'))

    return render(request, 'dashboard/pages/newPortfolioItem.html', {'form': form})

@login_required(login_url='account_login', redirect_field_name='next')
def editPortfolioItem(request, id):
    portfolioItem = Portfolio.objects.get(pk=id)

    if not portfolioItem:
        raise Http404()

    form = PortfolioForm(
        data = request.POST or None,
        files = request.FILES or None,
        instance = portfolioItem
    )

    if form.is_valid():
        form.save()
        
        messages.success(request, 'Alteração salva com sucesso!')
        return redirect(reverse('dashboard:managePortifolio'))

    return render(request, 'dashboard/pages/editPortfolio.html', {'form': form})

@login_required(login_url='account_login', redirect_field_name='next')
def delete_from_Portifolio(request, id):
    item = Portfolio.objects.get(pk=id)
    item.delete()
    return redirect(reverse('dashboard:managePortifolio'))


# ---Slider---
@login_required(login_url='account_login', redirect_field_name='next')
def manageSlider(request):
    content = Slider.objects.all()
    return render(request, 'dashboard/pages/manageSlider.html', {'content':content})

@login_required(login_url='account_login', redirect_field_name='next')
def addSlide(request):
    form = SlideForm()

    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:manageSlider'))
    
    return render(request, 'dashboard/pages/newSlide.html', {'form': form})

@login_required(login_url='account_login', redirect_field_name='next')
def editSlide(request, id):

    slide = Slider.objects.filter(pk=id).first()

    if not slide:
        raise Http404()

    form = SlideForm(
        data = request.POST or None,
        files = request.FILES or None,
        instance = slide
    )
    
    if form.is_valid():
        slide.save()

        messages.success(request, 'Alteração salva com sucesso!')
        return redirect(reverse('dashboard:manageSlider'))

    return render(
        request,
        'dashboard/pages/editSlide.html',
        context={'form': form}
    )


@login_required(login_url='account_login', redirect_field_name='next')
def deleteSlide(request, id):
    item = Slider.objects.get(pk=id)
    item.delete()
    return redirect(reverse('dashboard:manageSlider'))

#--- Ours Clients ---
@login_required(login_url='account_login', redirect_field_name='next')
def manageOursClients(request):
    content = OursClients.objects.all()
    return render(request, 'dashboard/pages/manageOursClients.html', {'content':content})

@login_required(login_url='account_login', redirect_field_name='next')
def addOurClient(request):
    form = OurClientsForm()

    if request.method == 'POST':
        form = OurClientsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:manageOursClients'))
    
    return render(request, 'dashboard/pages/editOurClients.html', {'form': form})


@login_required(login_url='account_login', redirect_field_name='next')
def editOurClient(request, id):

    slide = OursClients.objects.filter(pk=id).first()

    if not slide:
        raise Http404()

    form = OurClientsForm(
        data = request.POST or None,
        files = request.FILES or None,
        instance = slide
    )
    
    if form.is_valid():
        slide.save()

        messages.success(request, 'Alteração salva com sucesso!')
        return redirect(reverse('dashboard:manageOursClients'))

    return render(
        request,
        'dashboard/pages/editOurClients.html',
        context={'form': form}
    )

@login_required(login_url='account_login', redirect_field_name='next')
def deleteOurClient(request, id):
    item = OursClients.objects.get(pk=id)
    item.delete()
    return redirect(reverse('dashboard:manageOursClients'))

@login_required(login_url='account_login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect(reverse('gauenPublic:home'))

@login_required(login_url='account_login', redirect_field_name='next')
def managePerfil(request):
    content = request.user
    print(content)
    return render(request, 'dashboard/pages/manageProfile.html', {'content':content})

@login_required(login_url='account_login', redirect_field_name='next')
def manageLinks(request):
    links = UsefulLinks.objects.all()
    context = {
        'links': links
    }
    return render(request, 'dashboard/pages/manageLinks.html', context)


@login_required(login_url='account_login', redirect_field_name='next')
def addLink(request):
    form = LinkForm
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:manageLinks'))
    
    return render(request, 'dashboard/pages/newLink.html', context)

@login_required(login_url='account_login', redirect_field_name='next')
def editLink(request, id):

    link = UsefulLinks.objects.filter(pk=id).first()

    if not link:
        raise Http404()

    form = LinkForm(
        data = request.POST or None,
        files = request.FILES or None,
        instance = link
    )
    
    if form.is_valid():
        link.save()

        messages.success(request, 'Alteração salva com sucesso!')
        return redirect(reverse('dashboard:manageLinks'))

    return render(
        request,
        'dashboard/pages/newLink.html',
        context={'form': form}
    )

@login_required(login_url='account_login', redirect_field_name='next')
def deleteLink(request, id):
    link = UsefulLinks.objects.get(pk=id)
    link.delete()
    return redirect(reverse('dashboard:manageLinks'))

