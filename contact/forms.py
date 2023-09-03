from django import forms

from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=63)
    user_message = forms.CharField(widget=forms.Textarea, max_length=767)
    user_email = forms.EmailField(max_length=63)
    captcha = CaptchaField()