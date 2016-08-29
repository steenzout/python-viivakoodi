# -*- coding: utf-8 -*-
"""UPC module.

:Provided barcodes: UPC-A
"""

from __future__ import unicode_literals

from .ean import EuropeanArticleNumber13

__docformat__ = 'restructuredtext en'


class UniversalProductCodeA(EuropeanArticleNumber13):
    """Initializes new UPC-A barcode. Can be rendered as EAN-13 by passing
    `True` to the `make_ean` argument.

    Args:
        upc (str): upc number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
        make_ean (bool): render barcode as EAN-13 with leading 0 (default: False).
    """

    name = 'UPC-A'

    digits = 11

    def __init__(self, upc, writer=None, make_ean=False):
        if make_ean:
            UniversalProductCodeA.digits = 12
            upc = '0' + upc
        self.upc = upc
        EuropeanArticleNumber13.__init__(self, upc, writer)

    def __unicode__(self):
        return self.upc

    __str__ = __unicode__


UPCA = UniversalProductCodeA
