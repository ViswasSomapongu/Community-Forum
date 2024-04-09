from django.forms import ModelForm
from .models import Thread, Reply

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('title','description')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
        self.fields['title'].widget.attrs.update({'class':'form-control'})   
        self.fields['description'].widget.attrs.update({'class':'form-control'}) 

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('message',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
        self.fields['message'].widget.attrs.update({'class':'form-control','rows':5})
