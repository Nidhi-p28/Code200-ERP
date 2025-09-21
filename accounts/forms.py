from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, College

class CollegeAdminSignupForm(UserCreationForm):
    college_name = forms.CharField(max_length=255)
    college_code = forms.CharField(max_length=50)
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    contact_email = forms.EmailField()
    contact_phone = forms.CharField(max_length=15)
    affiliation = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "admin"  # assign role automatically
        if commit:
            user.save()
            # create linked college
            College.objects.create(
                name=self.cleaned_data['college_name'],
                code=self.cleaned_data['college_code'],
                address=self.cleaned_data['address'],
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                pincode=self.cleaned_data['pincode'],
                contact_email=self.cleaned_data['contact_email'],
                contact_phone=self.cleaned_data['contact_phone'],
                affiliation=self.cleaned_data['affiliation'],
                admin=user,
            )
        return user 
    