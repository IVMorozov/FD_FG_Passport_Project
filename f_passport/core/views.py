from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Avg
from django.db.models import F
from .models import MO, StatisticsShort

class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ФД&ФГ" 
        context["MO"] = MO.objects.all()     
        fd = StatisticsShort.objects.values("MO2").annotate(avg_F=Avg('F')).annotate(avg_FG=Avg('FG')).annotate(avg_Pop_Per=Avg('Pop_Per')).annotate(path_class=F('MO__path_class'))
        context["FD"] = fd
        context["js"] = list(fd)  # Преобразуем QuerySet в список для JSON
        return context
