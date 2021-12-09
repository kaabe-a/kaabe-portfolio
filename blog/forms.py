from django.forms import ModelForm, TextInput, EmailInput,Textarea,FileInput,Select
from . models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title':TextInput(attrs ={
                # 'class':'w50',
                'placeholder':'Post Title'
            }),
            'slug':TextInput(attrs ={
                # 'class':'w50',
                'placeholder':'Post Slug'
            }),
            'status':Select(attrs ={
                # 'class':'w50',
                'placeholder':'Choose One'
            }),
            'author':Select(attrs ={
                # 'class':'w50',
                'placeholder':'Choose One'
            }),
             'image':FileInput(attrs ={
                # 'class':'w50',
                'placeholder':'Post Slug'
            }),
            'body':Textarea(attrs = {
                # 'class':'w100',
                'placeholder':'Enter Your Post'
            })
        }