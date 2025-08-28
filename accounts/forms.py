from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User

class Register(UserCreationForm):
    error_messages = {
        "password_mismatch": _("As senhas não coincidem. Verifique e tente novamente."),
    }

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "photo"]
        labels = {
            "username": _("Nome de Usuário"),
            "email": _("E-mail"),
            "first_name": _("Primeiro Nome"),
            "last_name": _("Último Nome"),
            "password1": _("Senha"),
            "password2": _("Confirme a Senha"),
            "photo": _("Foto de Perfil"),
        }
        help_texts = {field: None for field in fields}
        error_messages = {
            "username": {
                "required": _("O nome de usuário é obrigatório."),
                "unique": _("Esse nome de usuário já existe. Escolha outro."),
            },
            "email": {
                "invalid": _("Digite um endereço de e-mail válido."),
                "required": _("O e-mail é obrigatório."),
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove todos os help_text padrões do Django
        for field in self.fields.values():
            field.help_text = None
        # Força username como obrigatório (mesmo que já seja no model)
        self.fields['username'].required = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "photo"]
        labels = {
            "username": _("Nome de Usuário"),
            "first_name": _("Primeiro Nome"),
            "last_name": _("Último Nome"),
            "photo": _("Foto de Perfil"),
        }
        help_texts = {
            "username": None,
            "first_name": None,
            "last_name": None,
            "photo": None,
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_("Esse nome de usuário já está em uso."))
        return username


