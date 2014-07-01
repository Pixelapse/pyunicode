# -*- coding: utf-8 -*-

# Default libs
import logging

# Installed libs

# Project modules

logger = logging.getLogger(__name__)


def safely_decode(unicode_or_str, encoding='utf-8'):
  ''' Decodes <str> into <unicode>. Ignores any non-utf8 chars in <str>s '''
  if isinstance(unicode_or_str, unicode):
    ustr = unicode_or_str
  elif isinstance(unicode_or_str, str):
    ustr = unicode_or_str.decode(encoding, 'ignore')
  else:
    raise Exception(u'Not of type unicode or str')

  return ustr
