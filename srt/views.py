from django.shortcuts import render

# Create your views here.
from .models import Subtitles
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import DetailView
from .form import SubmitForm
from .proj.tasks import srt
import pdb

class SubtitlesView(ListView):
    template_name = 'task/subtitles.html'
    model = Subtitles
    def get_queryset(self):
        filter_val = self.request.session['search_text']
        print(filter_val,'KUZCO')
        return Subtitles.objects.filter(subtitles__icontains=filter_val)

# A page with the form where we can pull video from s3 and generate srt file
class SubmitFormView(FormView):
    #pdb.set_trace()
    template_name = 'task/search_subtitle.html'
    form_class = SubmitForm
    def form_valid(self,form):
        av_name = form.cleaned_data.get('av_name')
        search_text = form.cleaned_data.get('search_text')
        srt.delay(av_name,search_text)
        messages.success(self.request, 'generating subtitles as celery task')
        self.request.session['search_text'] = search_text
        return redirect('subtitles')
