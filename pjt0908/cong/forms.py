from django import forms
from .models import Maru

#form class
# - 모델에 없는 값을 입력받고 싶을 때 

#modelform class
# - 모델이 있는 값만 입력받고 싶을 때 
class MaruForm(forms.ModelForm):
    #이 클래스를 설명하는 클래스 - Meta
    class Meta:
        model = Maru
        #사용자의 입력을 원하는 필드종류
        fields = '__all__'
        #exclude