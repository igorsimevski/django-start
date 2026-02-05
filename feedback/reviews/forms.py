from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="Your name", min_length=2, error_messages={
    "required": "Your name must not be empty",
    "min_length": "Longer please"
  })
  review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
  rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)