# from django import forms
# from .models import User

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name']
from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'center', 'fathername', 'mothername', 'email', 'phone','whatsapp','medium']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add a field for the center selection
        self.fields['center'] = forms.ModelChoiceField(queryset=Center.objects.all(), empty_label="Select")
        
        #self.fields['center'].initial = None

        # Customize field labels
        self.fields['name'].label = "Candidate's Name"
        self.fields['fathername'].label = "Father's Name"
        self.fields['mothername'].label = "Mother's Name"
        self.fields['center'].label = "Select Center"
        self.fields['email'].label = "Email ID"
        self.fields['phone'].label = "Contact Number"
        self.fields['whatsapp'].label = "WhatsApp Number"
        self.fields['medium'].label = "Medium of Examination"

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['fathername'].widget.attrs['class'] = 'form-control'
        self.fields['mothername'].widget.attrs['class'] = 'form-control'
        self.fields['center'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['whatsapp'].widget.attrs['class'] = 'form-control'
        self.fields['medium'].widget.attrs['class'] = 'form-control'



class RegistrationNumberForm(forms.Form):
    registration_number = forms.CharField(label='Enter Registration Number', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['registration_number'].widget.attrs['class'] = 'form-control'