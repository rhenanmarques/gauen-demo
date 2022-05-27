from gauenPublic.models import Price, UTILIZATION
import simplejson as json

class ConstructResp:
    '''
    Constroi resposta para o simulador
    '''
    def __init__(self, nameUT, category):
        self.__nameUT = nameUT
        self.__category = category
    
    def resposta(self):

        #Consulta ao BD
        for ut in UTILIZATION:
            if ut[1] == self.__nameUT:
                utID = ut[0]
                break
        #utID =  Utilizacao.objects.get(title= self.__nameUT).id
        preco = Price.objects.values('price').get(utilization= utID, categories= self.__category)

        return {'id_UT': utID, 'name_UT': self.__nameUT, 'cat':self.__category, 
                'price': json.dumps(preco['price'], use_decimal=True)}

class CheckCookies:
    '''
    Verifica a existencia de cookies, se não houver adiciona ao contexto a notificação 
    '''
    def __init__(self, request, context):
        cookies = request.COOKIES.get('GauenCookie')
        if not cookies:
            context['show_notification'] = True