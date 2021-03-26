from django import forms
from .models import Users
from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': '이메일을 입력해주세요'
    },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        password = clean_data.get('password')
        re_password = clean_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                user = Users(
                    email=email,
                    password=make_password(password),
                )
                user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': '이메일을 입력해주세요'
    },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        clear_data = super().clean()
        email = clear_data.get('email')
        password = clear_data.get('password')

        if email and password:
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                self.add_error('email', '이메일이 없습니다.')
                return
            if not (check_password(password, user.password)):
                self.add_error("password", "패스워드가 일치하지 않습니다.")
            else:
                self.email = user.email
