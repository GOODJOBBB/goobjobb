from django.forms import ModelForm 
from .models import Firstapp



class MemoForm(ModelForm):

    class Meta:
        model = Firstapp
        fields = ("company",'address','URL','pic',"telephone",'representative') 
