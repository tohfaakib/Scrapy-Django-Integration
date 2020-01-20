# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from test_app.models import Quotes


class QuotesItem(DjangoItem):
    django_model = Quotes
