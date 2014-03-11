#!/usr/bin/env python
#encoding:utf-8

"""
Here's a UI module that I use; you need a count of your total results, as well as the results for the page (this doesn't limit those results for you, if just builds the pagination links)
This code is from:http://stackoverflow.com/questions/15981257/can-tornado-handle-pagination
"""

from __future__ import division
import math
import urlparse
import urllib

import tornado.web

def update_querystring(url, **kwargs):
    base_url = urlparse.urlsplit(url)
    query_args = urlparse.parse_qs(base_url.query)
    query_args.update(kwargs)
    for arg_name, arg_value in kwargs.iteritems():
        if arg_value is None:
            if query_args.has_key(arg_name):
                del query_args[arg_name]
    query_string = urllib.urlencode(query_args, True)     
    return urlparse.urlunsplit((base_url.scheme, base_url.netloc,base_url.path, query_string, base_url.fragment))

class Paginator(tornado.web.UIModule):
"""Pagination links display."""

    def render(self, page, page_size, results_count):
        pages = int(math.ceil(results_count / page_size)) if results_count else 0

        def get_page_url(page):
            # don't allow ?page=1
            if page <= 1:
                page = None
            return update_querystring(self.request.uri, page=page)

        next = page + 1 if page < pages else None
        previous = page - 1 if page > 1 else None

        return self.render_string('uimodules/pagination.html', page=page, pages=pages, next=next,previous=previous, get_page_url=get_page_url)

"""
Here's the module template (uimodules/pagination.html in the above example):
"""
"""
{% if pages > 1 %}
<div class="pagination pagination-centered">
  <ul>
    <li{% if previous %}><a href="{{ get_page_url(previous) }}">&laquo;</a>{% else %} class="disabled"><span>&laquo;</span></li>{% end %}  
    {% for page_num in xrange(1, pages + 1) %}{# 1-index range #}
    <li{% if page_num != page %}><a href="{{ get_page_url(page_num) }}">{{ page_num }}</a>{% else %} class="active"><span>{{ page_num }}</span></li>{% end %}
    {% end %}
    <li{% if next %}><a href="{{ get_page_url(next) }}">&raquo;</a>{% else %} class="disabled"><span>&raquo;</span></li>{% end %}  
</ul>
</div>
{% end %}
"""

"""
Don't forget to tell your tornado app about the module.

Finally, to actually use it:

{% for result in results %}
<p>{{ result }}</p>
{% end %}
{% module Paginator(page, page_size, results_count) %}

"""
