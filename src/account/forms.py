from django import forms

from account.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)  # no save to database
        user.set_password(self.cleaned_data['password'])  # password should be hashed!
        user.is_active = False   # user cannot login
        user.save()

        activation_code = user.activation_codes.create()
        activation_code.send_activation_code()
        return user
