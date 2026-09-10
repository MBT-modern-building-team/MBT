from django.shortcuts import render
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from MBTApp import mbt_orm


def blog(request):
    lang = request.LANGUAGE_CODE
    data = {
        'title': _('Blog'),
        'subTitle': _('Blog'),
        'articles': mbt_orm.get_articles(lang),
    }
    return render(request, "news/blog.html", data)


def articleDetail(request, slug):
    lang = request.LANGUAGE_CODE
    article = mbt_orm.get_article_by_slug(slug, lang)
    if article is None:
        raise Http404(_("Artykuł nie istnieje"))
    article = dict(article)
    import re
    text = article.get('text', '')
    paras = [p.strip() for p in re.split(r'(?=(?:Wprowadzenie|Roboty ziemne|Podsumowanie|Ekspresowa budowa|Początek roku|Jeszcze dekadę temu|Zarządzanie|Planowanie|Budowa|Inwestycja|Koszt|Certyfikaty|Ekologia|BREEAM|Rynek|Ceny))', text) if p.strip()]
    if len(paras) < 2:
        paras = [text[i:i+400].strip() for i in range(0, len(text), 400) if text[i:i+400].strip()]
    article['paras'] = paras
    data = {
        'title': article['title'],
        'subTitle': _('Blog'),
        'article': article,
        'articles': mbt_orm.get_articles(lang),
    }
    return render(request, "news/blogDetails.html", data)