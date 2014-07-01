# -*- coding: utf-8 -*-

# Default libs
import logging

# Installed libs

# Project modules

logger = logging.getLogger(__name__)


def safely_decode(unicode_or_str, encoding='utf-8'):
  ''' Decodes byte <str> into <unicode>. Ignores any non-utf8 chars in <str>s '''
  if isinstance(unicode_or_str, unicode):
    ustr = unicode_or_str
  elif isinstance(unicode_or_str, str):
    ustr = unicode_or_str.decode(encoding, 'ignore')
  else:
    raise Exception(u'Not of type unicode or str')

  return ustr


def safely_encode(unicode_or_str, encoding='utf-8'):
  ''' Encodes <unicode> into byte <str>. Replaces any non utf8 chars '''
  if isinstance(unicode_or_str, unicode):
    rstr = unicode_or_str.encode(encoding, 'replace')
  elif isinstance(unicode_or_str, str):
    rstr = unicode_or_str
  else:
    raise Exception(u'Not of type unicode or str')

  return rstr
