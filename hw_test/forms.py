from django import forms

class TestMessageRecieve(forms.Form):

    hello_title = forms.CharField(label="Test title field", max_length=10)
    hello_body = forms.CharField(label="Test body field")
