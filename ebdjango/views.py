# coding=utf-8
import json

from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext

from ebdjango.models import TVSetting

from django.core import serializers


def index(request):
    return HttpResponse("Welcome to sample django app"
                        "<br>Please check the following:"
                        "<br>"
                        "<ul>"
                        "<li><a href=\"api/tvsettings/\">api/tvsettings/</a></li>"
                        "<li><a href=\"api/dynamic/tvsettings/\">api/dynamic/tvsettings/</a></li>"
                        "<li><a href=\"api/static/tvsettings/\">api/static/tvsettings/</a></li>"
                        "<li><a href=\"admin/\">admin/</a></li>"
                        "</ul>"
                        )

    # Leave the rest of the views (detail, results, vote) unchanged


def index2(request):
    template = loader.get_template("ebdjango/index.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def example(request):
    template = loader.get_template("ebdjango/index2.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def coming_soon(request):
    template = loader.get_template("ebdjango/coming_soon.html")
    title_string = "This is a title"
    context = RequestContext(request, {
        'title': title_string,
    })
    return HttpResponse(template.render(context))


def tvsettings(request):
    return JsonResponse({'color': 'blue',
                         'size': 5,
                         'theme': 'dark',
                         'featuredApps': [1, 2, "youtube", 5.0],
                         'themeURL': 'https://www.istockphoto.com/pl/zdj%C4%99cie/golden-cebuli-na-drewnianym-tle-rustykalnym-gm480134211-36493838'})


def dynamic_tvsettings(request):
    some_queryset = TVSetting.objects.all()

    serialized_queryset = serializers.serialize('python', some_queryset)
    dict_to_show=dict(serialized_queryset[0]['fields'])
    del dict_to_show['jsonPure']
    return JsonResponse(dict_to_show)


def static_tvsettings(request):
    tvSettingObject = TVSetting.objects.first()
    data = json.loads(tvSettingObject.jsonPure)
    what_to_show = data if data else  {"nothing_to_show": "Check if tvSettingObject  has proper .jsonPure param "}
    return JsonResponse(what_to_show, safe=False)

def get_cards(request):
    path_to_cards_file = './static/ebdjango/resources/results.txt'

    with open(path_to_cards_file) as json_file:
        data = json.load(json_file)

    what_to_show = data if data else  {"nothing_to_show": True}
    # list_of_cards=[]
    # for karta in data:
    #    list_of_cards.append(karta)
    #
    # newlist = sorted(list_of_cards, key=lambda k: k['nazwa'])

    return JsonResponse(what_to_show, safe=False)
