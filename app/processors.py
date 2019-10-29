from .models import get_listeners, get_speakers


def globals(request):
    return {
        "listeners": get_listeners(),
        "speakers": get_speakers()
    }
