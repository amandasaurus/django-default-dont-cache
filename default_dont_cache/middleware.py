class DefaultDontCacheMiddleware(object):
    """
    A middleware that will mark every request as not to be cached.
    This allows one to use the Django (Update|FetchFrom)CacheMiddleware
    middlewares without having caching turned on for every view. This allows an
    opt-in cache, not opt-out

    This middleware *must* be after/under the ``FetchFromCacheMiddleware``.
    """

    def process_request(self, request):
        request._cache_update_cache = False

