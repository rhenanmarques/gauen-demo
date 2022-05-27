
def habitacionais(altura, pisosAbaixoRef):

    if altura <= 9 and pisosAbaixoRef <= 1:
        return 1
    elif altura <= 28 and pisosAbaixoRef <= 3:
        return 2
    elif altura <= 50 and pisosAbaixoRef <= 5:
        return 3
    else:
        return 4


def estacionamentos(altura, pisosAbaixoRef, areaBruta, arLivre=False):

    if arLivre:
        return 1
    elif altura <= 9 and pisosAbaixoRef <= 1 and areaBruta <= 3200:
        return 1
    elif altura <= 28 and pisosAbaixoRef <= 3 and areaBruta <= 9600:
        return 2
    elif altura <= 28 and pisosAbaixoRef <= 5 and areaBruta <= 32000:
        return 3
    else:
        return 4


def administrativos(altura, efetivo):
    
    if altura <= 9 and efetivo <= 100:
        return 1
    elif altura <= 28 and efetivo <= 1000:
        return 2
    elif altura <= 50 and efetivo <= 5000:
        return 3
    else:
        return 4


def escolares_Hospitalares(altura=float, efetivo=int, localRiscoD=False, localRiscoE=False, efetivoLocaisRisco=0):
    
    if (localRiscoD or localRiscoE):

        if altura <= 9 and efetivo <= 100 and efetivoLocaisRisco <= 25:
            return 1
        elif altura <= 9 and efetivo <= 500 and efetivoLocaisRisco <= 100:
            return 2
        elif altura <= 28 and efetivo <= 1500 and efetivoLocaisRisco <= 400:
            return 3
        else:
            return 4
    else:

        if altura <= 9 and efetivo <= 100 and efetivoLocaisRisco <= 25:
            return 1
        elif altura <= 9 and efetivo <= 750 and efetivoLocaisRisco <= 100:
            return 2
        elif altura <= 28 and efetivo <= 2250 and efetivoLocaisRisco <= 400:
            return 3
        else:
            return 4  


def espetaculos_Desportivos(altura, pisosAbaixoRef, efetivo, arlivre=False):
    
    if arlivre:
        if efetivo <= 1000:
            return 1
        elif efetivo <= 1500:
            return 2
        elif efetivo <= 40000:
            return 3
        else:
            return 4
    else:
        if altura <= 9 and pisosAbaixoRef == 0 and efetivo <= 100:
            return 1
        elif altura <= 28 and pisosAbaixoRef <= 1 and efetivo <= 1000:
            return 2
        elif altura <= 28 and pisosAbaixoRef <= 2 and efetivo <= 5000:
            return 3
        else:
            return 4


def restauracao_Hotelaria(altura, efetivo, efetivoLocaisRisco=0):
    
    if altura <= 9 and efetivo <= 100 and efetivoLocaisRisco <= 50:
        return 1
    elif altura <= 9 and efetivo <= 500 and efetivoLocaisRisco <= 200:
        return 2
    elif altura <= 28 and efetivo <= 1500 and efetivoLocaisRisco <= 800:
        return 3
    else:
        return 4


def comerciais(altura, pisosAbaixoRef, efetivo):
    
    if altura <= 9 and pisosAbaixoRef == 0 and efetivo <= 100:
        return 1
    elif altura <= 28 and pisosAbaixoRef <= 1 and efetivo <= 1000:
        return 2
    elif altura <= 28 and pisosAbaixoRef <= 2 and efetivo <= 5000:
        return 3
    else:
        return 4


def museus_GaleriasArte(altura, pisosAbaixoRef, efetivo, arLivre=False):

    if arLivre:

        if efetivo <= 1000:
            return 1
        elif efetivo <= 15000:
            return 2
        elif efetivo <= 40000:
            return 3
        else:
            return 4

    else:

        if altura <= 9 and pisosAbaixoRef == 0 and efetivo <= 100:
            return 1
        elif altura <= 28 and pisosAbaixoRef <= 1 and efetivo <= 1000:
            return 2
        elif altura <= 28 and pisosAbaixoRef <= 2 and efetivo <= 5000:
            return 3
        else:
            return 4    
    

def bibilitecas_Arquivos(altura, pisosAbaixoRef, efetivo, cargaIncendio):
    # é necessario calculos e inputs adicionais
    if altura <= 9 and pisosAbaixoRef == 0 and efetivo <= 100 and cargaIncendio <= 5000:
        return 1
    elif altura <= 28 and pisosAbaixoRef <= 1 and efetivo <= 500 and cargaIncendio <= 50000:
        return 2
    elif altura <= 28 and pisosAbaixoRef <= 2 and efetivo <= 1500 and cargaIncendio <= 150000:
        return 3
    else:
        return 4


def Industrais_oficinas(cargaIncendio, pisosAbaixoRef, arLivre=False, exclusivArmaz=False):
    '''Quando a UT XII for exclusivamente destinada a armazenamento os
valores limite da densidade de carga de incêndio podem ser multiplicados por 10.'''
    
    if arLivre:
        if exclusivArmaz:
            if cargaIncendio <= 10000 and pisosAbaixoRef == 0:
                return 1
            elif cargaIncendio <= 100000 and pisosAbaixoRef <= 1:
                return 2
            elif cargaIncendio <= 300000 and pisosAbaixoRef <= 1:
                return 3
            else:
                return 4
        else:#Não exclusivo de armazenamento
            if cargaIncendio <= 1000 and pisosAbaixoRef == 0:
                return 1
            elif cargaIncendio <= 10000 and pisosAbaixoRef <= 1:
                return 2
            elif cargaIncendio <= 30000 and pisosAbaixoRef <= 1:
                return 3
            else:
                return 4

    else:#Integrado ao edificio
        if exclusivArmaz:
            if cargaIncendio <= 5000 and pisosAbaixoRef == 0:
                return 1
            elif cargaIncendio <= 50000 and pisosAbaixoRef <= 1:
                return 2
            elif cargaIncendio <= 150000 and pisosAbaixoRef <= 1:
                return 3
            else:
                return 4
        else:#Não exclusivo de armazenamento
            if cargaIncendio <= 500 and pisosAbaixoRef == 0:
                return 1
            elif cargaIncendio <= 5000 and pisosAbaixoRef <= 1:
                return 2
            elif cargaIncendio <= 15000 and pisosAbaixoRef <= 1:
                return 3
            else:
                return 4
