from django import forms
from newspaper.models import Comment, Contact,NewsLetter

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["post", "content"]

class NewsletterForm(forms.ModelForm):  


    class Meta:
        model = NewsLetter
        fields = "__all__" 