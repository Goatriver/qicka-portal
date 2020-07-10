from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    context = {
        "blocks": {
            "home": render_to_string("homepage/home.html"),
            "portfolio": render_to_string("portfolio/portfolio.html")
        }
    }

    return render(request, "homepage/index.html", context)
