#response_form/views.py
import sys
sys.path.insert(0,'..')

from django.shortcuts import render
from django.forms.models import ModelForm
from .models import ResponseModel
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from slam.questions_and_answers import fields as f 
from slam.questions_and_answers import create_message


class ResponseForm(ModelForm):
    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user', None)
        super(ResponseForm, self).__init__(*args, **kwargs)
        if user:
            for key, value in f.items():
                self.fields[key].help_text = getattr(user, key + '-H')
                #self.fields[key].help_text = getattr(user, key + '-Q')
    class Meta:
        model = ResponseModel
        exclude = ('author', 'submit_count')

@login_required
def ResponseFormView(request):
    def mail():
        subject = 'Thank you! Greetings from Pritam'
        res_ans = []
        for key in f.keys():
            res_ans.append(getattr(submission, key))
        message = create_message(res_ans)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email,]
        send_mail( subject, message, email_from, recipient_list )
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            request.user.count += 1
            submission.submit_count = request.user.count
            request.user.save()     
            submission.save()
            mail()
            print(submission)
            return render(request, 'thanks.html', {})
    else:
        form = ResponseForm(user=request.user)
        return render(request, 'response_tem.html', {'form': form})




