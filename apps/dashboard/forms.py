from django.forms import ModelForm
from .models import FieldOfStudy

class FieldOfStudyForm( ModelForm ):

    class Meta:

        model = FieldOfStudy

        fields = [ 'title', 'description' ]