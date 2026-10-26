from django import forms
from django.forms import ModelForm
from .models import FieldOfStudy

class FieldOfStudyForm( ModelForm ):


    class Meta:

        model = FieldOfStudy

        fields = [ 'title', 'description', 'image_icon' ]

        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "subject-form__input"}),
        #     'description':forms.Textarea(attrs={"class":  })
        # }
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
            'image_icon':forms.FileInput(attrs=
            {
                'id':"subject-icon",
                'name':"subject_icon",
                'accept':".png,.jpg,.jpeg,.svg"
            })
        }
