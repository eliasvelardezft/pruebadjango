from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'nacimiento',
            'dni'
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese su nombre',
                    'style': 'border-radius: 8px;'
                }
            )
        }

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if len(dni) < 8:
            raise forms.ValidationError('El dni es muy corto.')
        return dni
    
