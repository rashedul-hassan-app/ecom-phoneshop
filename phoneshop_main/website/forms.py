from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class '] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted">Please give a strong password</span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Please re-enter the same password</span>'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category',
                  'description', 'image', 'is_sale', 'sale_price']
        # widgets = {
        #     'description': forms.Textarea(attrs={
        #         'rows': 1
        #     }
        #     )
        # }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['name'].widget.attrs['placeholder'] = ''
        self.fields['name'].label = 'Product Name'
        self.fields['name'].help_text = ''

        self.fields['price'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['price'].widget.attrs['placeholder'] = 'Product price'
        self.fields['price'].label = 'Product Price'
        self.fields['price'].help_text = ''

        self.fields['category'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['category'].widget.attrs['placeholder'] = 'Product category'
        self.fields['category'].label = 'Product category'
        self.fields['category'].help_text = ''

        self.fields['description'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['description'].widget.attrs['placeholder'] = ''
        self.fields['description'].label = 'Product description'
        self.fields['description'].help_text = ''

        self.fields['image'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['image'].widget.attrs['placeholder'] = 'Product image'
        self.fields['image'].label = 'Please upload a product image'
        self.fields['image'].help_text = ''

        self.fields['is_sale'].widget.attrs['class '] = 'form-check-input form-control-gray'
        self.fields['is_sale'].widget.attrs['placeholder'] = 'Sale Price'
        self.fields['is_sale'].label = 'On SALE '
        self.fields['is_sale'].help_text = ''

        self.fields['sale_price'].widget.attrs['class '] = 'form-control form-control-gray'
        self.fields['sale_price'].widget.attrs['placeholder'] = 'Sale price'
        self.fields['sale_price'].label = 'Sale Price'
        self.fields['sale_price'].help_text = ''
