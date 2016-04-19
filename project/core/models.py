# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_date = models.DateTimeField(verbose_name=u'Дата', default=datetime.datetime.now,
                            editable=True)
  class Meta:
    verbose_name = u'Страница'
    verbose_name_plural = u'Страницы'

  def __unicode__(self):
    return _(u'Страница: ') + self.title


