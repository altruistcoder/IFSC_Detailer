from django import forms


class Submit_ifsc(forms.Form):
    ifsc = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the IFSC code",
                "class": "form-control"
            }
        )
    )
