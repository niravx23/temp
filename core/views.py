from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.core.mail import send_mail


from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

from django.contrib.auth import logout

def loggingOut(request) : 
        logout(request)
        return  redirect("/login/")

def subscribe(request):
    email = request.GET.get('email', '')  # Get the 'email' parameter from the URL

    # You can now use the 'email' variable in your view logic
    # For example, you can store it in a database, send a confirmation email, etc.
    subject = 'Welcome To Het community'
    message = f'Thank you for registering in Het Community.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )

    return render(request ,  'core/subscribe.html' , {'email' : email})