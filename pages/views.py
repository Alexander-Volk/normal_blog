from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404

from .models import Page


def get_page(request, url):
    if not url.startswith('/'):
        url = '/' + url
    try:
        page = get_object_or_404(Page, slug=url, published=True)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            page = get_object_or_404(Page, slug=url, published=True)
            return HttpResponsePermanentRedirect(f'{request.path}/')
        else:
            raise
    return render_page(request, page)


def render_page(request, page):
    if page.registration_required and not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    return render(request, page.template, context={'page': page})
