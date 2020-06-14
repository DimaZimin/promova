from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Ім'я")
    from_email = forms.EmailField(required=True, label="Електронна пошта")
    subject = forms.CharField(required=True, label="Тема")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':'70','rows':'4'}), required=True, label="Повідомлення")