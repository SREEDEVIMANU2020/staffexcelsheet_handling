from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['emp_id', 'consultant_name', 'company_email', 'role']
        widgets = {
            'emp_id': forms.TextInput(attrs={'class': 'form-control'}),
            'consultant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user