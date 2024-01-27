from django import forms
from .models import Item


class ItemPictureForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'quantity', 'picture']

    picture = forms.ImageField(widget=forms.ClearableFileInput())