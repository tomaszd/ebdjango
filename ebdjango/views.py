from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext


def index(request):
    return HttpResponse("bababababaaba12334")

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
                         'featuredApps':[1,2,"youtube",5.0],
                         'themeURL': 'https://www.istockphoto.com/pl/zdj%C4%99cie/golden-cebuli-na-drewnianym-tle-rustykalnym-gm480134211-36493838'})
