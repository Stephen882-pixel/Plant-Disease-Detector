from django import forms
from .models import LeafImage

class LeafImageForm(forms.ModelForm):
    class Meta:
        model = LeafImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }