from django.contrib.auth import get_user_model
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'