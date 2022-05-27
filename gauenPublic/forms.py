from django import forms
from .models import Map, Locale, LocalMaterial, Message
from utils.gauenPublic.djangoForms import add_attr, add_placeholder
from django.core.exceptions import ValidationError



class SimulatorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SimulatorForm, self).__init__(*args, **kwargs)

        self.fields['utilizacao_Tipo'].widget.attrs['class'] = 'form-select'
        self.fields['efetivo_Local_D'].widget.attrs['class'] = 'form-select'
        self.fields['efetivo_Local_E'].widget.attrs['class'] = 'form-select'


        add_placeholder(self.fields['altura'], 'Ex.: 3')
        add_placeholder(self.fields['subsolo'], 'Ex.: 1')
        add_placeholder(self.fields['area_Bruta'], 'Ex.: 355,95')
        add_placeholder(self.fields['efetivo_Total'], 'Ex.: 25')
        add_placeholder(self.fields['efetivo_Local_D'], 'Ex.: 30')
        add_placeholder(self.fields['efetivo_Local_E'], 'Ex.: 30')

    
    class Meta:
        model = Map
        fields = [
        'utilizacao_Tipo',
        'altura',
        'subsolo',
        'ar_Livre',
        'area_Bruta',
        'efetivo_Total',
        'carga_Incendio',
        'armazenExclusiv',
        'local_Risco_D',
        'local_Risco_E',
        'efetivo_Local_D',
        'efetivo_Local_E',
        ]


class Ambiente(forms.ModelForm):

    class Meta:
        model = Locale
        fields = [
            'nome_Ambiente',
            'area_Ambiente',
            'finalidade',
            ]

class Materiais(forms.ModelForm):
    
    class Meta:
        model = LocalMaterial
        fields = (
            "material",
            "volume")

class MapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MapForm, self).__init__(*args, **kwargs)

        # Set class
        for field in (
            'nome_Estabelecimento',
            'morada_Estabelecimento',
            'email',
            'telefone'):
            self.fields[field].widget.attrs['class'] = 'form-control'
             
        self.fields['concelho'].widget.attrs['class'] = 'form-select'
        
        self.fields['agree_to_terms'].widget.attrs['class'] = 'form-check-input'
        self.fields['agree_to_terms'].widget.attrs['required'] = True
        self.fields['im_aware_it'].widget.attrs['class'] = 'form-check-input'
        self.fields['im_aware_it'].widget.attrs['required'] = True

        #set label

        self.fields['agree_to_terms'].label = "Estou de acordo com os termos de utilização de serviço"
        self.fields['im_aware_it'].label = "Estou ciente que o valor apresentado é referente aos honorários de elaboração das medidas de autoproteção, não incluidos os valores referente a taxas de analise ANEPC."
            

        #set paceholder
        add_placeholder(self.fields['nome_Estabelecimento'], 'Ex.: Pingo Doce')
        add_placeholder(self.fields['morada_Estabelecimento'], 'Ex.: Avenida da República')
        add_placeholder(self.fields['email'], 'Ex.: email@email.com')
        add_placeholder(self.fields['telefone'], 'Ex.: 930000000')


        """for fieldname in ['utilizacao_Tipo', 'categoria', 'nome_Estabelecimento', 'morada_Estabelecimento', 'numero_Fiscal', 'email', 'telefone']:
            self.fields[fieldname].help_text = 'Olá'"""
        #help_text
        #self.fields['email'].help_text = 'Informe um e-mail válido'

        #error_text
        #self.fields['email'].error_messages = 'Informe um e-mail válido'

    class Meta:
        model = Map
        fields = [
            'nome_Estabelecimento',
            'morada_Estabelecimento',
            'concelho',
            'email',
            'telefone',
            'im_aware_it',
            'agree_to_terms',
        ]
        widgets = {
            'telefone': forms.TextInput(attrs={'data-mask': "000-000-000"}),
            #'im_aware_it': forms.BooleanField(required=True)
        }

        """error_messages = {

        }"""


class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        add_placeholder(self.fields['name'], 'Nome')
        add_placeholder(self.fields['email'], 'Email')
        add_placeholder(self.fields['phone'], 'Telefone')
        add_placeholder(self.fields['describe'], 'Assunto')
        add_placeholder(self.fields['message'], 'Mensagem')
    
    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'phone',
            'describe',
            'message', 
        ]

