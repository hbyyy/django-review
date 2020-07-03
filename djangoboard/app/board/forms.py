from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(max_length=64,
                            label='제목을 입력하세요',
                            error_messages={
                                'required': '제목을 입력해주세요'
                            },
                            widget=forms.TextInput(attrs={
                                'class': 'form-control'
                            }))
    contents = forms.CharField(label='내용',
                               error_messages={
                                   'required': '내용을 입력하세요'
                               },
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
