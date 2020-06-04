from django.forms import ModelForm

from news.models import News


class CreateNews(ModelForm):
    class Meta:
        model = News
        fields = ['name','pic','category','body_text','short_text']