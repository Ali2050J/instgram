from django import forms


class CreateCommentForm(forms.Form):
    body = forms.CharField()
