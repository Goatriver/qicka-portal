from django.conf import settings


def constants(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        "SOCIALS": settings.TEMPLATE_CONSTANTS['SOCIALS'],
        "MENU": settings.TEMPLATE_CONSTANTS['MENU_LINKS']
    }

