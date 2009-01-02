#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by Pradeep Gowda on 2009-01-01.
Copyright (c) 2009 Pradeep Gowda. All rights reserved.
"""
from __future__ import division
from pyofc2 import *
import time   
import math 
import random
import inspect
from jinja import Environment, FileSystemLoader

def test_line():      
    '''  
    Line
    Simple Line Graph
    '''
    t = title(text=time.strftime('%a %Y %b %d'))
    l = line()
    l.values = [9,8,7,6,5,4,3,2,1]
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l)
    return chart 

def frange(a,b,incr):
    lst = []
    while a <= b:
        lst.append(a)
        a += incr
    return lst
    
def test_line_dot():
    '''
    Line Dot
    Examples of Dotted Line Chart
    '''
    t = title(text=time.strftime('%a %Y %b %d'))     
    l1 = line_dot()
    l1.values = map(lambda x: math.sin(x)*1.9 + 7, frange(0,6.2, 0.2))
    l1.halo_size = 0
    l1.width = 2
    l1.dot_size = 4
    
    l2 = line_dot()
    l2.values = map(lambda x: math.sin(x)*1.9 + 10, frange(0,6.2, 0.2))
    l2.halo_size = 1
    l2.width = 1
    l2.dot_size = 4
    
    l3 = line_dot()
    l3.values = map(lambda x: math.sin(x)*1.9 + 4, frange(0,6.2, 0.2))
    l3.halo_size = 1
    l3.width = 6
    l3.dot_size = 4
                   
    y = y_axis()
    y.min, y.max, y.steps = 0, 15, 5
    
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l1)
    chart.add_element(l2)    
    chart.add_element(l3)
    chart.y_axis = y
    return chart 


def test_line_hollow():
    '''
    Line Hollow 
    Examples of Hollow Line Charts  
    '''
    t = title(text=time.strftime('%a %Y %b %d'))     
    l1 = line_hollow()
    l1.values = map(lambda x: math.sin(x)*1.9 + 7, frange(0,6.2, 0.2))
    l1.halo_size = 0
    l1.width = 2
    l1.dot_size = 4

    l2 = line_hollow()
    l2.values = map(lambda x: math.sin(x)*1.9 + 10, frange(0,6.2, 0.2))
    l2.halo_size = 1
    l2.width = 1
    l2.dot_size = 4

    l3 = line_hollow()
    l3.values = map(lambda x: math.sin(x)*1.9 + 4, frange(0,6.2, 0.2))
    l3.halo_size = 1
    l3.width = 6
    l3.dot_size = 4

    y = y_axis()
    y.min, y.max, y.steps = 0, 15, 5

    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l1)
    chart.add_element(l2)    
    chart.add_element(l3)
    chart.y_axis = y
    return chart 

def test_manylines():
    '''
    Many Lines    
    Examples of Multiple Line Charts
    '''       
    l1 = line_dot()
    l1.width = 4
    l1.colour = "#DFC329"
    l1.dot_size = 5
    l1.values = [random.randint(1,6) for i in  range(9)]
    l1.text = 'Line 1'
    l1.font_size = 10
    
    l2 = line_hollow()
    l2.width = 1
    l2.colour = "#6363ac"
    l2.dot_size = 5
    l2.values = [random.randint(7,13) for i in  range(9)]  
    l2.text = 'Line 2'
    l2.font_size = 10
    
    l3 = line()
    l3.width = 4;
    l3.colour = "#5E4725"
    l3.values = [random.randint(14,19) for i in  range(9)]  
    l3.text = 'Line 3'
    l3.font_size = 10
    
    y = y_axis()
    y.min, y.max, y.steps = 0, 20, 5
    
    t = title(text='Three lines example') 
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l1)
    chart.add_element(l2)    
    chart.add_element(l3)
    chart.y_axis = y
    return chart      

def test_x_axis_labels_1():
    '''
    X Axis Labels 1
    
    Simple X Axis Lables
    '''
    t = title(text='X Axis Labels')
    l = line_dot()
    l.values = range(9,0,-1)
    
    x = x_axis()
    x.colour = '#428C3E'
    x.grid_colour = '#86BF83'
    lbl = labels(labels=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    x.labels = lbl
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l)
    chart.x_axis = x
    return chart

def test_x_axis_labels_3():
    '''
	X Axis Labels 3
	X Axis labels complex example
	'''
    t = title(text='X Axis Labels Complex Example')
    l = line_dot()
    l.values = range(9,0,-1)
    
    x = x_axis()
    x.stroke = 1
    x.colour = '#428C3E'
    x.tick_height = 5
    x.steps = 1
    x.grid_colour = '#86BF83'
    xlbls = x_axis_labels(steps=2, rotate='vertical', colour='#FF0000', size=16)

    lbls = ['one', 'two', 'three', 'four', 'five']
    lbls.append(x_axis_label(text='six', colour='#0000FF', size=30, rotate='vertical'))
    lbls.append(x_axis_label(text='seven', colour='#0000FF', size=30, rotate='vertical'))
    eight = x_axis_label(text='eight', colour='#8C773E', size=16, rotate='diagonal')
    eight.visible = True
    lbls.append(eight)
    lbls.append(x_axis_label(text='nine', colour='#2683CF', size=16, rotate='horizontal'))
    xlbls.labels = lbls
    x.labels = xlbls
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(l)
    chart.x_axis = x
    return chart

def _test():
    test_line()
    test_line_dot()
    test_line_hollow()
    test_manylines()
    test_x_axis_labels_1()
	
## The following functions are used to auto-generate demo files from this module.
def listfunc():
    me = __import__(inspect.getmodulename(__file__))
    for name in dir(me):
        obj = getattr(me, name)
        if inspect.isfunction(obj):
            yield obj

docs = [
    {'title':'Home', 
    'name':'index',
    'content':
    '''
    <p>pyOFC2 is a python library for <a href="http://teethgrinder.co.uk/open-flash-chart-2/">Open Flash Chart</a> 
    </p>

    <h3>Download and Install</h3> 
    <p>The source is available at <a href="">http://github.com/btbytes/pyofc2</a>. <br/>Use the <img src="http://assets2.github.com/images/modules/repos/download_button.png" /> button or use <code>git</code>
    <br/>
    <pre><code> $git clone git://github.com/btbytes/pyofc2.git </code></pre>   
    </p>
    ''' },
    ]
    
    
def build_examples():
    funcs = [f for f in listfunc() if f.__name__.startswith('test_')]
    examples = [] 
    for f in funcs:
        doc = ''.join([l.strip() for l in f.__doc__.split('\n')[2:]])
        doc = doc.replace('\n\n', '<br/>')
        doc = doc.replace('--', '</p><p>') 
        doc = '<p>%s</p>' % (doc, )  
        name = f.__name__.split('test_')[1]
        json = ''
        if f():
            json = f().render()
        code = inspect.getsource(f) 
        
        try:
            from pygments import highlight
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import HtmlFormatter

            lexer = get_lexer_by_name("python", stripall=True)
            formatter = HtmlFormatter(linenos=False, cssclass="syntax")
            code = highlight(code, lexer, formatter)
        except:
            pass 
        
        example = {
            'name': name,
            'title': f.__doc__.split('\n')[1].strip(),
            'doc': doc,
            'code': code,
            'datafile': 'data/%s.json' % (name, ),
            'json': json
            } 
        examples.append(example)
        
    #generate data files & sidebar links
    sidebar = '<ul>%s</ul>'
    links = []
    for e in examples:
        outf = open(e['datafile'], 'w')
        outf.write(e['json'])
        outf.close()     
        links.append('<li><a href="%s">%s</a></li>' %(e['name']+'.html', e['title']))      
    sidebar = sidebar % '\n'.join(links)
        
    #generate demo-html files
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('code.html')
    
    
    for e in examples:
        fname = e['name']+'.html'
        outf = open(fname, 'w')
        e.update({'sidebar':sidebar})
        output = tmpl.render(**e) 
        outf.write(output)
        outf.close()

    #generate doc-html files
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('doc.html')


    for e in docs:
        fname = e['name']+'.html'
        outf = open(fname, 'w')
        e.update({'sidebar':sidebar})
        output = tmpl.render(**e) 
        outf.write(output)
        outf.close()        
        
    print 'Build complete.'
    print 'Run ./start.sh and visit http://localhost:8000/'


if __name__ == '__main__':
    _test()
    build_examples()
    
    

