from django import forms
from django.forms import ModelForm
from .models import FieldOfStudy
from django.core.exceptions import ValidationError


class FieldOfStudyForm( ModelForm ):


    class Meta:

        model = FieldOfStudy

        fields = [ 'title', 'description', 'image_user', 'image_icon' ]

        widgets = {
            'title':forms.TextInput(attrs=
            {
                'id':"subject-name",
                'name' :"subject_name",
                'type':"text",
                'placeholder':"Например, Python, Django, Frontend"
            }),
            'description': forms.Textarea(attrs=
            {
                'id': "subject-description",
                'name': "subject_description",
                'placeholder':"Расскажи, чему хочешь научиться и какие цели у этого направления"
            }),
            'image_user':forms.FileInput(attrs=
            {
                'id':"subject-icon",
                'name':"subject_icon",
                'accept':".png,.jpg,.jpeg,.svg"
            })
        }
    def clean(self):

        cleaned_data = super().clean()

        if cleaned_data.get('image_user') and cleaned_data.get('image_icon'):
            raise ValidationError(
                "Выберите один способ задания иконки для направления"
            )

        return cleaned_data

