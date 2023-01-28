from django import forms

from utils import Utils


class RegisterForm(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8
    )

    def clean(self):
        super(RegisterForm, self).clean()

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not any(Utils.validate_password(password), Utils.validate_password(confirm_password)):
            self._errors.update(
                {
                    'password_typing': self.error_class([
                        'É preciso que sua senha tenha no mínimo uma letra maiúscula, um número e um caractere especial.'
                    ]) 
                }
            )

        if not password == confirm_password:
            self._errors.update(
                {
                    'password_match': self.error_class([
                        'As senhas não coincidem.'
                    ])
                }
            )

    