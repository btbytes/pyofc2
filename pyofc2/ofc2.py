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
        'grid_color': 'grid-colour', 'tick_height': 'tick-height', 'on_click':'on-click',
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

labels = ofc_factory('labels', ['labels'])
x_axis_label = ofc_factory('x_axis_label', ['text', 'steps', 'vertical', 'color', 'colour', 'size', 'visible', 'rotate' ])
x_axis_labels = ofc_factory('x_axis_labels', ['labels','steps', 'vertical', 'colour', 'color', 'size','rotate'])
  
axis =  ofc_factory('axis', ['stroke', 'tick_height', 'colour', 'grid_colour', 'steps', 'min', 'max', 'labels'])
class x_axis(axis): pass
class y_axis(axis): pass
class y_axis_right(axis): pass

tooltip = ofc_factory('tooltip', ['shadow', 'stroke', 'colour', 'bg_colour', 'title_style', 'body_style'])

element = ofc_factory('element', ['type','alpha', 'colour', 'color', 'text', 'fontsize', 'values'])
linefactory = ofc_factory('_line', ['type','alpha', 'colour','color', 'text', 
    'fontsize', 'values', 'halo_size', 'width', 'dot_size', 'on_click'])
line = lambda **kw: linefactory(type='line',**kw)     
line_dot = lambda **kw: linefactory(type='line_dot', **kw)
line_hollow = lambda **kw: linefactory(type='line_hollow', **kw)

bar = lambda **kw: element(type='bar',**kw)
bar_stack = lambda **kw: element(type='barstack',**kw)

class open_flash_chart(dict):               
    typetable = {
    'title': title,
    'x_legend':x_legend,
    'y_legend':y_legend,
    'x_axis': x_axis,
    'y_axis': y_axis,
    'y_axis_right': y_axis_right,
    'tooltip' : tooltip,
    }

    def __setattr__(self, k, w):
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
