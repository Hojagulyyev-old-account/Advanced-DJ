from django import forms

from .models import Product, Item

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data['title']

        if len(title) < 5:
            raise forms.ValidationError("title is too short")
        else:
            return title

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data['description']

        if len(description) < 5:
            raise forms.ValidationError("description is too short")
        else:
            return description

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title', )
