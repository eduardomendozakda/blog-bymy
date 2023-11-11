from django import forms
from .models import Wallpaper

class FormCreationWallpaper(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = (
            'title',
            'description',
            'category',
            'thumbnail',
            )