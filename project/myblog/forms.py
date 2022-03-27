
from logging import PlaceHolder
from random import choices
from xml.etree.ElementTree import Comment
from django import forms
from.models import Post

#choices=Category.objects.all().values_list('name','name')
#choice_list=[]

#for item in choices:
   # choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','header_photo','category','author','snippets','body')
        #cat=[('coding','coding'),('3d','3d'),('life','life'),('tech','tech')]

        #choices=Category.objects.all().values_list('name','name')

        Widgets={
            'title':forms.TextInput(attrs={'class':'form-control',}),
            'title_tag':forms.TextInput(attrs={'class':'form_control'}),
            'author':forms.Select(attrs={'class':'form_control'}),
            'category':forms.Select(attrs={'class':'form_control'}),
            'title':forms.Textarea(attrs={'class':'form_control'}),
            'snippets':forms.Textarea(attrs={'class':'form_control'})
        
        }

#class CommentForm(forms.ModelForm):
    #class Mata: 
      # model=Comment
      # fields='__ all __'
