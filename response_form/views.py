# response_form/views.py
import sys
sys.path.insert(0, '..')

from slam.questions_and_answers import fields as f
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import ResponseModel
from django.forms.models import ModelForm
from django.shortcuts import render
from django.forms.models import model_to_dict



class Sub:
    def __init__(self, label, help_text, value):
        self.label = label
        self.help_text = help_text
        self.value = value


class ResponseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ResponseForm, self).__init__(*args, **kwargs)
        if user:
            for key, value in f.items():
                self.fields[key].help_text = getattr(user, key + '-H')
                self.fields[key].label = getattr(user, key + '-Q')

    class Meta:
        model = ResponseModel
        exclude = ('author', 'submit_count')


@login_required
def ResponseFormView(request):
    def mail():
        subject = 'Thank you! Greetings from Pritam'
        data = []
        for key in f.keys():
            data.append(Sub(
                label=getattr(request.user, key+'-Q'),
                help_text=getattr(request.user, key+'-H'),
                value=getattr(submission, key)
            ))
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email, ]
        html_message = render_to_string(
            'mail_template.html', {'data': data})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, email_from,
                  recipient_list, html_message=html_message)
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            #submission.submit_count = request.user.count
            submission.save()
            # print(submission.id)
            request.user.last_response = submission.id
            request.user.save()
            mail()
            return render(request, 'thanks.html', {})
    else:
        try:
            prev_data = ResponseModel.objects.get(id=request.user.last_response)
        except Exception as e:
            print(e)
            prev_data = None
        form = ResponseForm(instance=prev_data, user=request.user)
        return render(request, 'response_tem.html', {'form': form})
