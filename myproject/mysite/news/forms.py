from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content', 'time_created', }
        widgets = {
            'title': forms.TextInput(attrs={'class':'a1'}),
            'content': forms.Textarea(attrs={'class':'a2'})
        }

class SendMail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'abc', 'id':'idxxx'}))
    cc = forms.BooleanField(required=False)

