from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from srt.views import SubmitFormView, SubtitlesView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('subtitles/', SubtitlesView.as_view(), name='subtitles'),
    url('search_subtitle/', SubmitFormView.as_view(), name='search_subtitle')
]
