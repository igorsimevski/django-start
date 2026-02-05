from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="Your name", min_length=2, error_messages={
    "required": "Your name must not be empty",
    "min_length": "Longer please"
  })