from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Talk, User
from django.core.exceptions import VakidationError

TABOO_WORDS = ["ばか", "バカ", "あほ", "アホ"]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)

    def cleam_message(self):
        message = self.cleaned_data["message"]
        matched = [w for w in TABOO_WORDS if w in message]
        if matched:
            raise ValidationError(f"禁止ワード{', '.join(matched)}が含まれています")
        return message
class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email": "新しいメールアドレス"}
        help_texts = {"email": ""}