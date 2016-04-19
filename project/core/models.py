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


class Knowledges(models.Model):
  skill_name = models.CharField(verbose_name=u'Умение', max_length=250)
  skill_level = models.IntegerField(
        verbose_name=u'Уровень', 
        help_text=u'Оценка своих знаний по этому предмету по шкале от 0 до 10',
        default=0)

  class Meta:
    verbose_name = u'Знание'
    verbose_name_plural = u'Знания'

  def __unicode__(self):
    return _(u'Знание: ') + self.skill_name


class Adverts(models.Model):
  i_want = models.ForeignKey(Knowledges, verbose_name=u'Я хочу научиться', related_name='skill_name1')
  i_can = models.ManyToManyField(Knowledges, verbose_name=u'Я умею', related_name='skill_name2')
  date_created = models.DateTimeField(verbose_name=u'Дата создания', default=datetime.datetime.now,
                            editable=True)
  date_modified = models.DateTimeField(verbose_name=u'Дата изменения', default=datetime.datetime.now,
                            editable=True)
  body = models.TextField()
  class Meta:
    verbose_name = u'Объявление'
    verbose_name_plural = u'Объявления'

  def __unicode__(self):
    return _(u'Объявление: Хочу научиться [') + self.i_want.skill_name + ']'



