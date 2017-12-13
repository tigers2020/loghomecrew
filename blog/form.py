from django import forms
from blog import models

class BlogForm(forms.ModelForm):
	class Meta:
		fields = ("blog_text", "themes")
		model = models.BlogText

		widgets= {
			'title':forms.TextInput(attrs={'class': 'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable dedium-editor-textarea'})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = models.BlogComments
		fields = ('author', 'text')