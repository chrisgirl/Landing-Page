from django import forms


class Form(forms.Form):
    name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        "class": 'form-control my-input',
        "name": "name",
        "id": "name",
        "placeholder": "Name"
    }))
    email = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": 'form-control my-input',
        "name": "title",
        "id": "title",
        "placeholder": "Email"
    }))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "style": "height:100px", "class": 'form-control my-input',
        "name": "content",
        "id": "content",
        "placeholder": "Content"
    }))