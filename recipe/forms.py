from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'author', 'description', 'tags']
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
            "placeholder": "Title"
        })
        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_image",
        })
        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_description",
            "placeholder": "Descriptions"
        })
        self.fields['tags'].widget.attrs.update({
            "class": "form-select",
            "id": "recipe_tags",
        })


    def clean_title(self):
        title = self.cleaned_data['title']
        return title.capitalize()



class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['recipe', 'title', 'quantity', 'unit', 'is_active']
        exclude = ['recipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_title",
            "placeholder": "Title"
        })
        self.fields['quantity'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_quantity",
            "placeholder": "Quantity"
        })
        self.fields['unit'].widget.attrs.update({
            "class": "form-select",
            "id": "ingredient_unit",
        })
        self.fields['is_active'].widget.attrs.update({
            # "class": "form-control",
            "id": "ingredient_is_active",
        })

