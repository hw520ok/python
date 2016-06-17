# -*- coding: utf-8
import lxml.etree

NSMAP = {None:'http://www.w3.org/2005/Atom'}

new_feed = lxml.etree.Element('feed',nsmap=NSMAP,attrib={'type':'root'})
title = lxml.etree.SubElement(new_feed,'title',nsmap={'dad':'dafs'},attrib={'type':'html'})
print(lxml.etree.tounicode(new_feed))

import xml.etree.ElementTree as etree2


feed2 = etree2.Element('{sdfds}feed',attrib={'p1':'v1'})

print(etree2.tostring(feed2))

