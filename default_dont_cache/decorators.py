from functools import wraps
from django.contrib import messages

def mark_for_caching(func):
    """
    Decorator that enabled caching for this page.
    It's similar to ``cache_page`` decorator, but will work with middlewares
    that set headers (e.g. LocaleMiddleWare, SessionMiddleware,
    AuthenticationMiddleware etc.)

    If a response has messages (from the django.contrib.messages) then it will
    not be cached.

    You must have the ``DefaultDontCacheMiddleware`` middleware
    """

    @wraps(func)
    def newfunc(request, *args, **kwargs):
        response = func(request, *args, **kwargs)

        # Only cache if there are no messages
        request._cache_update_cache = len(messages.get_messages(request)) == 0

        return response

    return newfunc

