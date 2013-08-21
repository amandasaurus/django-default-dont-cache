Opt-in caching for Django's per-site cache.

Django has a good 'whole page' caching system, the ['per-site' cache](https://docs.djangoproject.com/en/dev/topics/cache/#the-per-site-cache). However it is "opt-out". By default all pages are cached, and you mark pages not to be cached with the ``@never_cache`` decorator.

This app turns that Django cache into a 'opt-in' cache. By default pages will *not* be cached, unless you use the ``@mark_for_caching`` decroator.

Installation
============

    pip install django-default-dont-cache

Usage
=====

In your ``MIDDLEWARE_CLASSES`` setting:

    MIDDLEWARE_CLASSES = (
        …
        'django.middleware.cache.UpdateCacheMiddleware',
        …
        'django.middleware.cache.FetchFromCacheMiddleware',
        # This must be after the FetchFromCacheMiddleware
        'default_dont_cache.middleware.DefaultDontCacheMiddleware',
        …
    )

The ``DefaultDontCacheMiddleware`` *must* be after/below Django's ``FetchFromCacheMiddleware``.

By default none of your view will be cached by Django's caching system. You must manually whitelist views to be cached like so:

    from default_dont_cache.decorators import mark_for_caching
    
    @mark_for_caching
    def myview(request):
        …

Now ``myview`` will be cached by the django caching system. Only views that have the ``@mark_for_caching`` decorator will be cached.

Licence & Copyright
===================

© Rory McCann 2013, released under the GNU GPL v3 (or at your option a later verson). See the file LICENCE for more.
