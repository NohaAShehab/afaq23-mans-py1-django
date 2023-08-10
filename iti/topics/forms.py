from django import forms
from topics.models import Topic

class TopicForm(forms.Form):
    name =  forms.CharField(label='Topic Name' , max_length=100)
    logo = forms.ImageField(label='Topic logo')




class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name','logo']


    # def save(self, commit=True):
    #     pass

