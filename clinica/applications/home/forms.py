from django import forms

from applications.clientes.models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = {
            'name',
            'email',
            'phone',
            'message',
        }
    
        widgets ={
            'name': forms.TextInput(attrs={'class': 'u-grey-10 u-input u-input-rectangle form-control', 'placeholder': 'Ingrese nombre completo', 'id': 'valiname'}),
            'email': forms.EmailInput(attrs={'class': 'u-grey-10 u-input u-input-rectangle form-control', 'placeholder': 'Ingrese correo', 'id': 'valiemail'}),
            'phone': forms.TextInput(attrs={'class': 'u-grey-10 u-input u-input-rectangle form-control bg-gradient-info', 'placeholder': 'Ingrese numero de celular', 'id': 'validationServerUsername'}),
            'message': forms.Textarea(attrs={'class': 'u-grey-10 u-input u-input-rectangle form-control', 'placeholder': 'Ingrese mensaje', 'id': 'valimessage'})
        }


        
