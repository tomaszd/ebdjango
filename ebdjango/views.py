# coding=utf-8
import json

import os
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, RequestContext
from rest_framework import viewsets

from ebdjango.forms import MatchResultForm
from ebdjango.models import TVSetting, Player, MatchResult
from ebdjango.serializers import PlayerSerializer
from .serializers import MatchResultSerializer


def index(request):
    return HttpResponse("Welcome to sample django app"
                        "<br>Please check the following:"
                        "<br>"

                        "<br>TVSettings"
                        "<ul>"
                        "<li><a href=\"api/tvsettings/\">api/tvsettings/</a></li>"
                        "<li><a href=\"api/dynamic/tvsettings/\">api/dynamic/tvsettings/</a></li>"
                        "<li><a href=\"api/static/tvsettings/\">api/static/tvsettings/</a></li>"
                        "</ul>"
                        "<br>Cards"
                        "<ul>"
                        # "<li><a href=\"api/cards/\">api/cards/</a></li>"
                        "<li><a href=\"api/dynamic/cards/\">api/dynamic/cards/</a></li>"
                        "<li><a href=\"api/resources/\">api/resources/</a></li>"
                        "</ul>"
                        "<br>PING PONG!"
                        "<ul>"
                        "<li><a href=\"pingpong/players\">pingpong/players</a></li>"
                        "<li><a href=\"pingpong/results\">pingpong/results</a></li>"
                        "<li><a href=\"pingpong/results/new\">pingpong/results/new</a></li>"
                        "<li><a href=\"pingpong/results/new\">pingpong/results/ID</a></li>"
                        "</ul>"
                        "<br>ADMIN"
                        "<ul>"
                        "<li><a href=\"admin/\">ADMIN/</a></li>"
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
    dict_to_show = dict(serialized_queryset[0]['fields'])
    del dict_to_show['jsonPure']
    return JsonResponse(dict_to_show)


def static_tvsettings(request):
    tvSettingObject = TVSetting.objects.first()
    data = json.loads(tvSettingObject.jsonPure)
    what_to_show = data if data else  {"nothing_to_show": "Check if tvSettingObject  has proper .jsonPure param "}
    return JsonResponse(what_to_show, safe=False)


def pingpong_players(request):
    response = "Here are the list of Players:"
    response += "<ul>"
    for player in Player.objects.all():
        response += "<li>" + str(player) + "</li>"
    response += "</ul>"
    return HttpResponse(response
                        )


def pingpong_results_static(request):
    response = "Here are the list of Match Results:"
    response += "<ul>"
    for result in MatchResult.objects.all():
        response += "<li>" + str(result) + "</li>"
    response += "</ul>"
    return HttpResponse(response
                        )


def pingpong_results(request):
    template = loader.get_template("ebdjango/all_results.html")
    context = RequestContext(request, {
        'match_results': MatchResult.objects.all(),
    })
    return HttpResponse(template.render(context))


def get_cards(request):
    path_to_cards_file = './static/ebdjango/resources/res__ults.txt'

    with open(path_to_cards_file) as json_file:
        data = json.load(json_file)

    what_to_show = data if data else  {"nothing_to_show": True}
    # list_of_cards=[]
    # for karta in data:
    #    list_of_cards.append(karta)
    #
    # newlist = sorted(list_of_cards, key=lambda k: k['nazwa'])

    return JsonResponse(what_to_show, safe=False)


def get_the_most_recent_result():
    result_dir = "./static/ebdjango/resources/"

    a = [s for s in os.listdir(result_dir)
         if os.path.isfile(os.path.join(result_dir, s)) and "result" in s]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(result_dir, s)))
    print "result", a
    return os.path.join(result_dir, a[-1])


def dynamic_get_cards(request):
    path_to_cards_file = get_the_most_recent_result()

    # path_to_cards_file = './static/ebdjango/resources/res__ults.txt'
    with open(path_to_cards_file) as json_file:
        json_data = json.load(json_file)

    with_cena = []
    without_cena = []
    total_money = 0.0
    for singlekarta in json_data:
        if 'cena' in singlekarta:
            singlekarta['cena'] = float(singlekarta['cena'].replace(",", "."))

            if singlekarta['cena'] < 0.5:
                singlekarta['cena'] = 0.5

            with_cena.append(singlekarta)
            total_money += singlekarta['cena'] * singlekarta['ilosc']
        else:
            singlekarta['cena'] = "NO PRICE YET!"
            without_cena.append(singlekarta)

    with_cena = sorted(with_cena, key=lambda k: k['cena'])[::-1]
    template = loader.get_template("ebdjango/all_cards.html")
    context = RequestContext(request, {
        'json_cards_with_price': with_cena,
        # 'json_cards_tojs': json.dumps(with_cena),
        'cards_no_price': without_cena,
        'total_money': total_money
    })
    return HttpResponse(template.render(context))


def get_resources_files_path(request):
    result_dir = "./static/ebdjango/resources/"
    result_dir_on_server = "/home/ec2-user/Results/"
    a = []
    if os.path.isdir(result_dir):
        a = [s for s in os.listdir(result_dir)
             if os.path.isfile(os.path.join(result_dir, s))]

        a.sort(key=lambda s: os.path.getmtime(os.path.join(result_dir, s)))
        a = [result_dir + " :"] + a
    b=["There is no path : "+result_dir_on_server]
    if os.path.isdir(result_dir_on_server):
        b = [s for s in os.listdir(result_dir_on_server)
             if os.path.isfile(os.path.join(result_dir_on_server, s))]
        b.sort(key=lambda s: os.path.getmtime(os.path.join(result_dir_on_server, s)))
        b = [result_dir_on_server + " :"] + b

    html_content = "User :"+os.getlogin()

    for resource_path in a:
        html_content += "<li>" + resource_path + "</li>"

    for resource_path in b:
        html_content += "<li>" + resource_path + "</li>"

    print html_content
    return HttpResponse("Our_Resources files:"
                        "<ul>"
                        + html_content +
                        "</ul>"
                        )


def result_new(request):
    if request.method == "POST":
        form = MatchResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.author = request.user
            result.save()
            return redirect('pingpong_results')
        else:
            return redirect('pingpong_results')
    else:

        form = MatchResultForm()

    return render(request, 'ebdjango/result_new.html', {'form': form})


def result_edit(request, pk):
    result = get_object_or_404(MatchResult, pk=pk)
    if request.method == "POST":
        form = MatchResultForm(request.POST, instance=result)
        if form.is_valid():
            result = form.save(commit=False)
            result.author = request.user
            result.save()
            return redirect('pingpong_results')
    else:
        form = MatchResultForm(instance=result)
    return render(request, 'ebdjango/result_edit.html', {'form': form})


def results_list(request):
    if request.method == 'GET':
        match_results = MatchResult.objects.all()
        serializer = MatchResultSerializer(match_results, many=True)
        print serializer.data
        return JsonResponse(serializer.data, safe=False)


class MatchResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
