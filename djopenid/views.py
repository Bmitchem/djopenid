from django.core.urlresolvers import reverse
from django.shortcuts import render

from djopenid import util


def index(request):
    consumer_url = reverse('consumer:startOpenID')
    server_url = reverse('server:server')

    return render(request, 'djopenid/index.html', {'consumer_url':consumer_url, 'server_url':server_url})

