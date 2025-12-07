from django import forms
from .models import Membership, Car, Addbook, sign1

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['fname', 'lname', 'age', 'address', 'cell']
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'First Name'
            }),
            'lname': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Last Name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Age'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Address'
            }),
            'cell': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Cell Phone'
            }),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price', 'seats', 'img', 'description']
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'e.g., Toyota'
            }),
            'model': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'e.g., Camry'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'e.g., 2024'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'e.g., 1500000'
            }),
            'seats': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'e.g., 5'
            }),
            'img': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Image URL'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Car description...',
                'rows': 4
            }),
        }

class AddbookForm(forms.ModelForm):
    class Meta:
        model = Addbook
        fields = ['author', 'title']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Author Name'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Book Title'
            }),
        }

class SignupForm(forms.ModelForm):
    class Meta:
        model = sign1
        fields = ['user', 'passw']
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Username'
            }),
            'passw': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent',
                'placeholder': 'Password'
            }),
        }
