from django import forms

from .models import Item

inputClasses = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': inputClasses
            }),
            'name': forms.TextInput(attrs={
                'class': inputClasses,
            }),
            'description': forms.Textarea(attrs={
                'class': inputClasses,
            }),
            'price': forms.TextInput(attrs={
                'class': inputClasses,
            }),
            'image': forms.FileInput(attrs={
                'class': inputClasses,
            })
        }