#!/usr/bin/env python
# encoding: utf-8
"""
ofc2.py

Created by Pradeep Gowda on 2009-01-01.
Copyright (c) 2009 Pradeep Gowda.
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import cjson

class OFCBase(dict):
    type = None
    replace = {
        'font_size':'font-size', 'fontsize': 'font-size',
        'color':'colour', 'bg_color':'bg_colour', 'bgcolor':'bg_colour',
        'dot_size': 'dot-size', 'dotsize':'dot-size', 'grid_colour': 'grid-colour',
        'dot_style': 'dot-style',
        'grid_color': 'grid-colour', 'tick_height': 'tick-height',
        'on_click':'on-click', 'outline_color':'outline-colour',
        'outline_colour':'outline-colour', 'fill_color':'fill',
        'fill_colour':'fill', 'fill_alpha':'fill-alpha',
        'halo_size':'halo-size', 'halosize':'halo-size',
        'proximity': 'mouse', 'spoke_labels':'spoke-labels'
    }

    def __setattr__(self, k, w):
        if k in self.acceptable:
            if k in self.replace.keys():
                k = self.replace[k]
            self[k] = w
            self.__dict__.update({k:w})


def ofc_init(self, **kw):
    for k,w in kw.items():
        if k in self.acceptable:
            if k in self.replace.keys():
                k = self.replace[k]
            self[k] = w
            self.__dict__.update({k:w})


def ofc_factory(classname, acceptable):
       klass = type(classname, (OFCBase, ), {'acceptable':acceptable})
       setattr(klass, '__init__', ofc_init )
       return klass

title = ofc_factory('title', ['text','style'])
class x_legend(title): pass
class y_legend(title): pass

labels = ofc_factory('labels', ['labels', 'text'])
x_axis_label = ofc_factory('x_axis_label', ['text', 'steps', 'color', 'colour', 'size', 'visible', 'rotate' ])
x_axis_labels = ofc_factory('x_axis_labels', ['labels', 'rotate', 'steps'])
radar_axis_labels = ofc_factory('radar_axis_labels', ['labels'])
radar_spoke_labels = ofc_factory('radar_spoke_labels',['labels'])
shapefactory = ofc_factory('_shape', ['type','colour', 'color', 'values'])
shape = lambda **kw: shapefactory(type='shape', **kw)
shape_value = ofc_factory('shape_value', ['x', 'y'])

axis =  ofc_factory('axis', ['stroke', 'tick_height', 'colour',
    'grid_colour', 'steps', 'min', 'max', 'labels', 'offset', 'radar',
    'spoke_labels'
    ])
class x_axis(axis): pass
class y_axis(axis): pass
class y_axis_right(axis): pass
class radar_axis(axis): pass

tooltip = ofc_factory('tooltip', ['shadow', 'stroke', 'colour', 'bg_colour', 'title_style', 'body_style', 'proximity'])

element = ofc_factory('element', ['type','alpha', 'colour', 'color', 'text', 'fontsize', 'values'])

entry = ofc_factory('values', ['text', 'fontsize', 'colour', 'color'])

linefactory = ofc_factory('_line', ['type','alpha', 'colour','color', 'text',
    'fontsize', 'font_size', 'values', 'halo_size', 'width', 'dot_size', 'on_click', 'tip',
    'loop', 'dot_style'])
line = lambda **kw: linefactory(type='line',**kw)
line_dot = lambda **kw: linefactory(type='line_dot', **kw)
line_hollow = lambda **kw: linefactory(type='line_hollow', **kw)

key = ofc_factory('key', ['text', 'size', 'colour', 'font-size'])
dot_value = ofc_factory('value', ['value', 'colour', 'color', 'tip'])
dotfactory = ofc_factory('_dot-style', ['type', 'dot_style', 'dot_size', 'halo_size', 'colour', 'rotation', 'hollow', 'on_click', 'style'])
dot = lambda **kw: dotfactory(type='solid-dot', **kw)
hollowdot = lambda **kw: dotfactory(type='hollow-dot', **kw)
stardot = lambda **kw: dotfactory(type='star', **kw)

barfactory = ofc_factory('_bar', ['type', 'values', 'alpha', 'color', 'colour', 'key', 'on_click'])
bar = lambda **kw: barfactory(type='bar',**kw)
barvalue = ofc_factory('values', ['colour', 'value', 'tip', 'top', 'bottom'])

barfilledfactory = ofc_factory('_bar', ['type', 'values', 'alpha', 'color',
    'colour', 'key', 'outline_colour', 'outline_color'])
bar_filled = lambda **kw: barfilledfactory(type='bar_filled',**kw)

hbarfactory = ofc_factory('_hbar', ['type', 'values', 'color', 'colour', 'tooltip', 'tip'])
hbar = lambda **kw: hbarfactory(type='hbar', **kw)
hbar_value = ofc_factory('hbar_factory', ['left', 'right', 'tip'])

barstackfactory = ofc_factory('_barstack', ['type', 'values', 'keys', 'tip', 'color', 'colours', 'on_click'])
bar_stack = lambda **kw: barstackfactory(type='bar_stack',**kw)

area_linefactory = ofc_factory('_area_line', ['type', 'values', 'color', 'colour',
    'tooltip', 'width', 'dot_size', 'dotsize', 'halo_size', 'halosize' 'key', 'fill_colour',
    'fill_color', 'fill_alpha', 'loop'])
area_line = lambda **kw: area_linefactory(type='area_line', **kw)
area_hollow = lambda **kw: area_linefactory(type='area_hollow', **kw)

scatter_value = ofc_factory('values', ['x','y'])
scatterfactory = ofc_factory('_scatter', ['type', 'dot_size', 'color', 'colour', 'values'])
scatter = lambda **kw: scatterfactory(type='scatter', **kw)
scatter_line = lambda **kw: scatterfactory(type='scatter_line', **kw)

pie_value = ofc_factory('values', ['label', 'label-color', 'font-size', 'tooltip', 'color', 'colour', 'value', 'tip', 'on_click'])
piefactory = ofc_factory('_pie', ['alpha', 'colour', 'color', 'text',
        'fontsize', 'values', 'start_angle', 'animate', 'colours', 'label_colour',
        'on_click', 'radius', 'type'])
pie = lambda **kw: piefactory(type='pie', **kw)

#TODO: derive open_flash_chart class from OFCBase . use ofc_factory
class open_flash_chart(OFCBase):
    typetable = {
    'title': title,
    'x_legend':x_legend,
    'y_legend':y_legend,
    'x_axis': x_axis,
    'y_axis': y_axis,
    'y_axis_right': y_axis_right,
    'tooltip' : tooltip,
    'radar_axis': radar_axis,
    }

    def __setattr__(self, k, w):
        super(OFCBase, self).__setattr__(k,w)
        if k in self.typetable.keys():
            assert(isinstance(w, self.typetable[k]))
        self[k] = w

    def add_element(self, element):
        try:
            self['elements'].append(element)
        except:
            self['elements'] = [element]

    def __str__(self):
        return cjson.encode(self)

    def render(self):
        return cjson.encode(self)
