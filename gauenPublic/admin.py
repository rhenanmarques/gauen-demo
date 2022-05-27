from django.contrib import admin
from import_export.admin import ImportExportModelAdmin #biblioteca permite configurar a exportação de arquivos de dados 

from .models import *

# Register your models here.

@admin.register(Concelho)
class ConcelhoAdmin(ImportExportModelAdmin):
    pass

@admin.register(UsefulLinks)
class UsefulLinksAdmin(admin.ModelAdmin):
    pass

@admin.register(Material)
class MaterialInline(ImportExportModelAdmin):
     pass
    
     
class LocalMaterial(admin.TabularInline):
    model = LocalMaterial
    extra = 1
    

@admin.register(Atividade)
class AtividadeInline(ImportExportModelAdmin):
    pass

class LocalAtividade(admin.TabularInline):
    model = LocalAtividade
    extra = 1

class ItenLocale(admin.ModelAdmin):
    
    inlines = [LocalMaterial, LocalAtividade]
    
admin.site.register(Locale, ItenLocale)



@admin.register(Utilizacao)
class TypeUtilizacao(admin.ModelAdmin):
    pass

@admin.register(Map)
class ItemMap(admin.ModelAdmin):
    pass


@admin.register(Price)
class ItemPrice(ImportExportModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


