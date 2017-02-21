from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="name", max_length=20, error_messages={
        'required': "input yourname",
        'max_length': 'name is too long'
    })

    content = forms.CharField(label='content', error_messages={
        'required': "input content",
        'max_length': "content is too long"
    })
