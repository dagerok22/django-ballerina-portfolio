from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    # class Meta:
    #     model = Message
    #     widgets = {
    #         'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'col-sm-5'}),
    #         'email': forms.EmailField(attrs={'placeholder': 'Email', 'class': 'col-sm-6 col-sm-offset-1'}),
    #         'message': forms.Textarea(
    #             attrs={'placeholder': 'Message', 'class': 'col-sm-12'}),
    #     }
    class Meta:
        model = Message
        fields = ["name", "email", "message"]

    name = forms.CharField(
        label=None,
        widget=forms.TextInput(
            attrs={'class': 'col-sm-5', 'placeholder': 'Name'}
        )
    )
    email = forms.CharField(
        label=None,
        widget=forms.EmailInput(
            attrs={'class': 'col-sm-6 col-sm-offset-1', 'placeholder': 'Email'}
        )
    )
    message = forms.CharField(
        label=None,
        widget=forms.Textarea(
            attrs={'class': 'col-sm-12', 'placeholder': 'Message..'}
        )
    )