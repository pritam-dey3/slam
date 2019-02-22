#response_form/views.py

from django.shortcuts import render
from django.forms.models import ModelForm
from .models import ResponseModel
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



class ResponseForm(ModelForm):
    class Meta:
        model = ResponseModel
        exclude = ('author', 'title','submit_count')

@login_required
def ResponseFormView(request):
    def mail():
        subject = 'Thank you! Greetings from Pritam'
        message = submission.text
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email,]
        send_mail( subject, message, email_from, recipient_list )
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
             #== author
            request.user.count += 1
            submission.submit_count = request.user.count
            submission.title = str(request.user) + str(submission.submit_count)  
            request.user.save()     
            submission.save()
            mail()
            #print(submission)
            return render(request, 'thanks.html')
    else:
        form = ResponseForm()
        return render(request, 'response_tem.html', {'form': form})
    def mail():
        subject = 'Thank you! Greetings from Pritam'
        message = submission.text
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email,]
        send_mail( subject, message, email_from, recipient_list )


'''

class CommandForm(ModelForm):
    class Meta:
        model = Command



# Create your views here.
from command.models import Command
from command.models import CommandForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf

def submitform(request):
    if request.method == "POST":
        form = CommandForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'newcommand.html')
    else:
        form = CommandForm()
        return render(request, 'inputtest.html', {'form': form})

'''


