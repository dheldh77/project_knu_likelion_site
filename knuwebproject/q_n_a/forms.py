from django import forms
from .models import QNA

# 만약 모델 기반이 아니라면 forms.Form
class QNAForm(forms.ModelForm):
    class Meta:
        model = QNA
        fields = ['title' , 'description']
    