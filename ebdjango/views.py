from django.http import HttpResponse


def index(request):
    return HttpResponse("bababababaaba")

    # Leave the rest of the views (detail, results, vote) unchanged
