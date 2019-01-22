from django.http import HttpResponse
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
