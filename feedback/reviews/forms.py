from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your name", min_length=2, error_messages={
#     "required": "Your name must not be empty",
#     "min_length": "Longer please"
#   })
#   review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # individual: ['user_name', 'review_text', 'rating']
        # exclude = ['owner_comment']
        labels = (
            {"user_name": "Your Name", "review_text": "Comment", "rating": "Rating"}
        )
        error_messages = {
            "user_name": {
                "required": "Must not be empty",
                "max_length": "Longer please 2",
            }
        }
