from django import forms

class MembershipForm(forms.Form):
    package=forms.CharField(max_length=20)
    amount=forms.IntegerField()