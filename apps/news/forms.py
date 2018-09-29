from django import forms

from pagedown.widgets import AdminPagedownWidget

from .models import Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), label=u"文章详细信息")

    class Meta:
        model = Article
        fields = "__all__"