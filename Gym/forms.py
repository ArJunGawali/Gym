from .models import img
from django import forms

class imgform(forms.ModelForm):
    class Meta:
        model = img
        fields = ('title', 'cover',)
        labels = {
			'title' : ('Security Code'),
			'cover' : ('Photo')
		}
        widgets = {
            'title': forms.PasswordInput(
				attrs={
					'class': 'form-control',
					'id': 'scode',
					}
				),
            
			}
		