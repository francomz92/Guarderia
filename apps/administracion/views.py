from django.views.generic.base import TemplateView

# Create your views here.


class Dashboard(TemplateView):
    template_name = 'dashboard.html'