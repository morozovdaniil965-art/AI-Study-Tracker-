from django import forms
from django.forms import ModelForm
from .models import FieldOfStudy
from django.core.exceptions import ValidationError


class FieldOfStudyForm( ModelForm ):
    icon_type = forms.ChoiceField(
        choices=[
            ('default', 'Выбрать из стандартных'),
            ('custom', 'Загрузить свою иконку'),
        ]
    )

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
                'placeholder':"Расскажи, чему хочешь научиться и какие цели у этого направления",
                'maxlength': 300,
            }),
            'image_user':forms.FileInput(attrs=
            {
                'id':"subject-icon",
                'name':"subject_icon",
                'accept':".png,.jpg,.jpeg,.svg"
            }),

        }
    def clean(self):

        cleaned_data = super().clean()

        icon_type = cleaned_data.get('icon_type')
        image_icon = cleaned_data.get('image_icon')
        image_user = cleaned_data.get('image_user')

        if bool( image_user) == bool( image_icon) :
            raise ValidationError(
                "Выберите один способ задания иконки для направления"
            )

        return cleaned_data

