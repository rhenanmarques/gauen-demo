from blog.models import Post
from django import forms
from gauenPublic.models import UsefulLinks
from utils.gauenPublic.djangoForms import add_attr, add_placeholder

from dashboard.models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        """for fd in ('title','description', 'cover', 'cover_describ', 'category'):
            self.fields[fd].widget.attrs['class'] = 'form-control'"""
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['article'].widget.attrs['class'] = 'form-control'
        self.fields['cover'].widget.attrs['class'] = 'form-control'
        self.fields['cover'].widget.attrs['onchange'] = 'loadFile(event)'
        self.fields['cover_describ'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'

        self.fields['title'].label = "Título"
        self.fields['description'].label = "Subtitulo"
        self.fields['article'].label = "Artigo"
        self.fields['cover'].label = "Capa"
        self.fields['cover_describ'].label = "Descrição capa"
        self.fields['is_published'].label = "Publicado"
        self.fields['category'].label = "Categoria"


        add_placeholder(self.fields['title'], 'Título')
        add_placeholder(self.fields['description'], 'Subtitulo')
        add_placeholder(self.fields['article'], 'Artigo')
        add_placeholder(self.fields['category'], 'Selecione a categoria')


    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'cover',
            'cover_describ',
            'article',
            'category',
            'is_published',
        ]

        widgets = {'cover': forms.FileInput(),} 

class PortfolioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['onchange'] = 'loadFile(event)'
        self.fields['is_Public'].widget.attrs['class'] = 'form-check-input'
        self.fields['describ'].widget.attrs['class'] = 'form-control'

        self.fields['title'].label = "Título"
        self.fields['describ'].label = "Descrição"
        self.fields['image'].label = "Imagem"
        self.fields['is_Public'].label = "Público"

        add_placeholder(self.fields['title'], 'Título')
        add_placeholder(self.fields['describ'], 'Descreva o assunto a que se relaciona a imagem')
        add_placeholder(self.fields['image'], 'Imagem')
        add_placeholder(self.fields['is_Public'], 'Público')

    class Meta:
        model = Portfolio
        fields = [
            'image',
            'title',
            'describ',
            'is_Public'
        ]
        widgets = {'image':forms.FileInput(),}

class SlideForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SlideForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['onchange'] = 'loadFile(event)'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title_animation'].widget.attrs['class'] = 'form-control'
        self.fields['title_animation_duration_in'].widget.attrs['class'] = 'form-control'
        self.fields['subtitle'].widget.attrs['class'] = 'form-control'
        self.fields['subtitle_animation'].widget.attrs['class'] = 'form-control'
        self.fields['subtitle_animation_duration_in'].widget.attrs['class'] = 'form-control'
        self.fields['button_name'].widget.attrs['class'] = 'form-control'
        self.fields['button_link'].widget.attrs['class'] = 'form-control'
        self.fields['button_animation'].widget.attrs['class'] = 'form-control'
        self.fields['button_animation_duration_in'].widget.attrs['class'] = 'form-control'

        self.fields['image'].label = "Capa(tamanho máximo 1 mb)"
        self.fields['title'].label = "Título"
        self.fields['title_animation'].label = "Animação título"
        self.fields['title_animation_duration_in'].label = "Duração animação título"
        self.fields['subtitle'].label = "Subtitilo"
        self.fields['subtitle_animation'].label = "Animação subtítulo"
        self.fields['subtitle_animation_duration_in'].label = "Duração animação subtítulo"
        self.fields['button_name'].label = "Nome do botão"
        self.fields['button_link'].label = "URL"
        self.fields['button_animation'].label = "Animação botão"
        self.fields['button_animation_duration_in'].label = "Duração animação botão"
    
    class Meta:
        model = Slider
        fields = [
            'image',
            'title',
            'title_animation',
            'title_animation_duration_in',#float
            'subtitle',
            'subtitle_animation',
            'subtitle_animation_duration_in',#float
            'button_name',
            'button_link',
            'button_animation',
            'button_animation_duration_in',
            'is_published'
        ]
        widgets = {
            'title_animation_duration_in': forms.NumberInput(attrs={'step': 0.1}),
            'subtitle_animation_duration_in': forms.NumberInput(attrs={'step': 0.1}),
            'button_animation_duration_in': forms.NumberInput(attrs={'step': 0.1}),
            'image': forms.FileInput(),
        }

class OurClientsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OurClientsForm, self).__init__(*args, **kwargs)

        self.fields['logo'].widget.attrs['class'] = 'form-control'
        self.fields['logo'].widget.attrs['onchange'] = 'loadFile(event)'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['logo'].label = "Logo (Altura ideal imagem: 160 px)"
        self.fields['name'].label = "Empresa ou Entidade"
        self.fields['is_activate'].label = "Público"

    class Meta:
        model = OursClients
        fields = [
            'logo',
            'name',
            'is_activate',
        ]

        widgets = {
            'logo': forms.FileInput(),
        }

class LinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)

        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['class'] = 'form-control'

        self.fields['label'].label = "Label para o link"
        self.fields['url'].label = "URL"

    class Meta:
        model = UsefulLinks
        fields = [
            'label',
            'url',
        ]
