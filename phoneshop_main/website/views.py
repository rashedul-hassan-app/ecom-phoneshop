from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Category, SubscribedUsers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProductForm, NewsletterForm, SendNewsletterForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
import random


def index(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You are now Signed in!"))
            return redirect('index')
        else:
            messages.error(
                request, ("Unable to sign in. Please check your details and try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.error(request, ("You have been logged out!"))
    return redirect('index')


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # log the user in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ('Registration successful. Welcome ' + username + '!'))
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                # for error in errors:
                error_message = ', '.join(errors)
                if field in ['password1', 'password2']:
                    error_message += '. Password must be 8 characters long'
                messages.error(
                    request, f'{field.capitalize()}: {error_message}')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})


def product(request, pk):
    images = [
        'assets/images/ad1.png',
        'assets/images/ad2.png',
        'assets/images/ad3.png',
        'assets/images/ad4.png',
        'assets/images/ad5.png',
        'assets/images/ad6.png',
        'assets/images/ad7.png',
    ]
    random_image = random.choice(images)

    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product, 'ad_img': random_image})


def category(request, foo):
    foo = foo.replace('-', ' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        if foo == 'All':
            products = Product.objects.all()
            category = 'All products'

        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.error(request, ("The category does not exist ..."))
        return redirect('index')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('index')
        else:
            messages.error(
                request, 'Error whilst saving product. Please try again.')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html')


def newsletters(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request, 'This email is already subscribed! Try a different email.')
            return render(request, 'newsletters.html', {'form': form})

        if not name or not email:
            messages.error(
                request, 'A name and a valid email is required to subscribe')
            return render(request, 'newsletters.html', {'form': form})

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return render(request, 'newsletters.html', {'form': form})

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(
            request, f'{email} was successfully subscribed to our newsletters')
        return redirect('/')
    else:
        form = NewsletterForm(request.POST)
    return render(request, 'newsletters.html', {'form': form})


def send_newsletters(request):
    if request.method == 'POST':
        form = SendNewsletterForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            receivers = form.cleaned_data['receivers'].split(',')
            email_message = form.cleaned_data['message']

            mail = EmailMessage(
                subject, email_message, f"PhoneShop <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, 'Email sent successfully')
            else:
                messages.error(request, 'ERROR: Unable to send the email')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/newsletters/send')

    form = SendNewsletterForm()
    form.fields["receivers"].initial = ','.join(
        [active.email for active in SubscribedUsers.objects.all()])

    return render(request, 'send_newsletters.html', {'form': form})
