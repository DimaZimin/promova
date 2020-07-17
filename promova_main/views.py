from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = f"Name: {form.cleaned_data['name']}\nE-mail: {from_email} \n\n{form.cleaned_data['message']}"
            try:
                send_mail(subject, message, from_email, ['nonexistingmail@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Повідомлення успішно відправлене. Дякуюємо, що сконтактувалися з нами!')
            return redirect('home')
        messages.error(request, 'Error.')
    return render(request, 'promova_main/home.html', {'form': form})

def success(request):
    return render(request, 'promova_main/success.html')