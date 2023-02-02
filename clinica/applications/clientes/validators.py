from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
import re

def phone_validation(value):
    regex = r"^9"
    result = re.match(regex, value)

    if not value.isnumeric() and result is None and len(value) != 9:
        salida = 'Debe tener solo números <br/> Debe iniciar con 9 <br/> Solo 9 digitos <br/> :('
        raise ValidationError(mark_safe(salida))
    else:
        if not value.isnumeric() and result is None:
            salida = 'Debe tener solo números <br/>Debe comenzar con 9'
            raise ValidationError(mark_safe(salida))
        else:
            if not value.isnumeric() and len(value) != 9:
                salida = 'Debe tener solo números <br/> Debe tener 9 digitos'
                raise ValidationError(mark_safe(salida))
            else:
                if result is None and len(value) != 9:
                    salida = 'Debe comenzar con 9 <br/> Debe tener 9 digitos'
                    raise ValidationError(mark_safe(salida))
                else:
                    if result is None:
                        salida = 'Debe comenzar con 9'
                        raise ValidationError(mark_safe(salida))
                    else:
                        if len(value) != 9:
                            salida = 'Debe tener 9 digitos'
                            raise ValidationError(mark_safe(salida))
                        else:
                            if not value.isnumeric():
                                salida = 'Debe tener solo números'
                                raise ValidationError(mark_safe(salida))
                    


    
def house_validation(value):
    regex = r"^(66)"
    result = re.match(regex, value)

    if result is None:
        raise ValidationError('Debe comenzar con: 66')
    
    new = value.replace(' ', '')

    new2 = new.split('6',2)

    if not new.isnumeric():
        raise ValidationError('Debe tener solo números')

    if len(new2[2]) != 6 and len(new2[2]) != 7:
        raise ValidationError('Debe tener 6 o 7 digitos despues del 66')



def text_validation(value):
    regex = r"^[a-zA-Zñ\s]+$"
    result = re.match(regex, value)
    if result is None:
        raise ValidationError('Debe tener solo texto')

    

