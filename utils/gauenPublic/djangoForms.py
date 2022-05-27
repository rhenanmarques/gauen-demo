from django.core.exceptions import ValidationError

def add_attr(field, attr_name, attr_new_val):
    '''Função permite adicionar atributo a um campo'''

    existing = field.widget.attrs.get(attr_name, '')
    field.widget. attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    '''Função adiciona placeholder a um campo'''
    add_attr(field, 'placeholder', placeholder_val)
