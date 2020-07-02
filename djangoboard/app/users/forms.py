from django import forms
from django.contrib.auth.hashers import check_password

from users.models import TestUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, required=True, label='사용자 이름',
                               error_messages={
                                   'required': '아이디를 입력해주세요'
                               },
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': '아이디를 입력하세요',
                               })
                               )
    password = forms.CharField(max_length=64, required=True, label='비밀번호',
                               error_messages={
                                   'required': '패스워드를  입력해주세요'
                               },
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': '비밀번호를 입력하세요',
                               })
                               )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                user = TestUser.objects.get(username=username)
                if not check_password(password, user.password):
                    self.add_error('password', '비밀번호가 틀렸습니다')
                else:
                    cleaned_data.setdefault('user_id', user.id)
            except TestUser.DoesNotExist:
                self.add_error('username', '없는 유저입니다')
        return cleaned_data
