from .celery import app
from . import srtparse
from ..models import Subtitles

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def srt(av_name,search_text):
    d =  srtparse.run_parse(av_name,search_text)
    d_len=len(d.keys())
    for i in d:
        Subtitles.objects.create(av_name=av_name,timerange=i,subtitles=d[i])
    return f"{d_len} subtitles searched for {search_text} with success!"

"""def create_random_user_accounts(total):
  for i in range(total):
     username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
     email = '{}@example.com'.format(username)
     password = get_random_string(50)
     User.objects.create_user(username=username, email=email, password=password)
  return '{} random users created with success!'.format (total)
"""
