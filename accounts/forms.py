from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class Register(UserCreationForm):
    
    class Meta:

        model=User
        fields=["username", "email", "first_name", "last_name", "password1", "password2", "photo"]


from django import forms
from .models import User

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "photo"]

    def clean_username(self):
        username = self.cleaned_data['username']
        # self.instance é o usuário que está sendo editado
        qs = User.objects.filter(username=username).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Esse username já existe.")
        return username