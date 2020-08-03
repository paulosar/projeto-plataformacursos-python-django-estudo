from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .models import Comment

from simplemooc.core.mail import send_email_template

class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome:', max_length=100)
    email = forms.EmailField(label='E-mail:')
    message = forms.CharField(label='Mensagem/Dúvida:', widget=forms.Textarea)

    def send_email(self, course):
        subject = '[%s] Contato' % course.name
        #message = 'Nome: %(name)s;E-mail:%(email)s;%(message)s'
        context = {
            'name':self.cleaned_data['name'],
            'email':self.cleaned_data['email'],
            'message':self.cleaned_data['message']
        }
        #message = message % context
        #send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
        template_email = 'courses/contact_email.html'
        send_email_template(subject, template_email, context, [settings.CONTACT_EMAIL])

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment',]
