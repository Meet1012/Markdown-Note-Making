from django import forms
from django.core.exceptions import ValidationError

class Upload_Form(forms.Form):
    file = forms.FileField()
    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            user_file = uploaded_file.name.split(".")
            if user_file[1] not in ["md", "txt"]:
                raise ValidationError("Only .md, .txt files are allowed.")
        return uploaded_file