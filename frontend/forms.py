from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'required' : 'required'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'id': 'email',
                    'required' : 'required'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'id': 'comment',
                    'required' : 'required',
                    'rows' : '8',


                }
            ),
        }



        

