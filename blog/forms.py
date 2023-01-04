from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        self.body = kwargs.pop('body', None)
        super().__init__(*args, **kwargs)

    def save(self):
        comment = Comment()
        comment.author = self.author
        comment.post = self.post
        comment.body = self.body
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        print(comment.body)
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]
