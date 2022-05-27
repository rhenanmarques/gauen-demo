from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.


ARCHITECTURE_DRAWING = (
    (1, "Possui em formato compatível com CAD"),
    (2, "Possui em outro formato digital ou analógico não compatível com CAD"),
    (3, "Não possui")
)

BOOLEAN_TEXT = (
    ('yes', "Sim"),
    ('no', "Não")
)

CATEGORIES = (
    (1, '1ª'),
    ( 2, '2ª'),
    (3, '3ª'),
    (4, '4ª'))

RAI = (
    (1, 'Baixo'),
    (1.5, 'Médio'),
    (2, 'Alto')
)

SPACE_ALLOCATION = (
    ('Armazenamento', 'Armazenamento'),
    ('Fabrico', 'Fabrico/Manuentenção')
)

UTILIZATION = (
    (1, 'Habitacionais'),
    (2, 'Estacionamentos'),
    (3, 'Administrativos'),
    (4, 'Escolares'),
    (5, 'Hospitalares e Lares de Idosos'),
    (6, 'Espectáculos e Reuniões Públicas'),
    (7, 'Hoteleiros e Restauração'),
    (8, 'Comerciais e Gares de Transportes'),
    (9, 'Desportivos e de Lazer'),
    (10, 'Museus e Galerias de Arte'),
    (11, 'Biblioteca de Arquivos'),
    (12, 'Industriais, Oficinas, e Armazéns')

)

class Concelho(models.Model):
    designacao = models.CharField(max_length=100)
    def __str__(self):
        return self.designacao

class Material(models.Model): #eu quero pegar todos os itens desta classe no locale
    material = models.CharField(max_length= 160)
    fabrico_CI = models.IntegerField(null=True, blank=True)# dados serão fornecidos pela manuela
    fabrico_Rai = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    armazem_CI = models.IntegerField(null=True, blank=True)
    armazem_Rai = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
     
    def __str__(self):
        return self.material

class Atividade(models.Model):
    '''Este modelo recebe os itens relacionados a fabrico/manutenção'''
    atividade = models.CharField(max_length=160)
    atividade_CI = models.IntegerField(null=True, blank=True)
    atividade_Rai = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.atividade 

class Locale(models.Model):
    nome_Ambiente = models.CharField(max_length= 128)
    area_Ambiente = models.DecimalField(max_digits=10, decimal_places=2)
    finalidade = models.CharField(max_length=25, choices= SPACE_ALLOCATION)
    
    def __str__(self):
        return self.nome_Ambiente


#tabela relacional
class LocalMaterial(models.Model):
    '''Tabela de relacionamento local material'''
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    local = models.ForeignKey(Locale, on_delete=models.SET_NULL, null=True)
    volume = models.DecimalField(max_digits= 12, decimal_places=2)

class LocalAtividade(models.Model):
    '''tabela de ralacionamento local atividade'''
    Atividade = models.ForeignKey(Atividade, on_delete=models.SET_NULL, null=True)
    local = models.ForeignKey(Locale, on_delete=models.SET_NULL, null=True)

class Utilizacao(models.Model):
    title = models.CharField(max_length=160)
    referencia = models.IntegerField()
    describ = models.TextField()

    def __str__(self):
        return self.title

class StatusOrder(models.Model):
    status = models.CharField(max_length=128)
    
    def __str__(self):
        return self.status

class Price(models.Model):
    utilization = models.IntegerField(choices=UTILIZATION, null= True)
    categories = models.CharField(max_length=25, choices=CATEGORIES)
    plus = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{str(self.utilization)} {str(self.categories)}ª Categoria"


class Map(models.Model):
    #------------------ Identication -------------------------------------
    nome_Estabelecimento = models.CharField(max_length= 160)
    morada_Estabelecimento = models.CharField(max_length= 160)
    concelho = models.ForeignKey(Concelho, on_delete=models.SET_NULL, null=True)
    postalCode = models.CharField(max_length=7, null= True)
    numero_Fiscal = models.CharField(max_length=9)
    responsavel_legal = models.CharField(max_length=148)
    data_Funcionamento = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)], null= True)
    email = models.EmailField(max_length=254, null= True)
    telefone = models.CharField(max_length=9, null= True)
    delegado_seguranca = models.CharField(max_length=160)
    elemento_seguranca = models.CharField(max_length=160)
    

    #------------------ Building features ---------------------------------
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ar_Livre = models.CharField(max_length=3, choices= BOOLEAN_TEXT, null=True)
    area_Bruta = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    arquitetura_disponivel = models.IntegerField(choices=ARCHITECTURE_DRAWING, null= True)
    armazenExclusiv = models.BooleanField(default=False, null=True)
    atividade = models.CharField(max_length=160)
    carga_Incendio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    efetivo_Local_D = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    efetivo_Local_E = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    efetivo_Total = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    local_Risco_D = models.CharField(max_length=3, choices= BOOLEAN_TEXT, null=True)
    local_Risco_E = models.CharField(max_length=3, choices= BOOLEAN_TEXT, null=True)
    subsolo = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    #ambiente = models.ManyToManyField(Locale)

    #-------------------- Request status ------------------------------------------
    status = models.ForeignKey(StatusOrder, on_delete=models.SET_NULL, null=True)
    orcamento_Data = models.DateField(auto_now_add= True, null= True)
    utilizacao_Tipo = models.IntegerField(choices=UTILIZATION, null= True)
    categoria = models.IntegerField(choices=CATEGORIES, null= True)
    fatorEspecial = models.BooleanField(default=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    criated_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    agree_to_terms = models.BooleanField(default=False)
    im_aware_it = models.BooleanField(default=False)

    #-------------------- Files ---------------------------------------------------


    def __str__(self):
        return self.nome_Estabelecimento

class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=9)
    describe = models.CharField(max_length=160)
    message = models.TextField()
    criated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.describe

class UsefulLinks(models.Model):
    label = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.label


