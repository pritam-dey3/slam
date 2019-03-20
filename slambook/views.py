from django.contrib.auth.views import LoginView
from slam.questions_and_answers import intro1

class myLoginView(LoginView):
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['intro'] = intro1
        return data