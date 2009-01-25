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
import pprint
from jinja import Environment, FileSystemLoader
import markdown2 #http://code.google.com/p/python-markdown2/

#utilitarian objects
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    'Nov', 'Dec']
    
def test_line():      
    '''  
    Line Charts/Line
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
    Line Charts/Line Dot
    Example of Dotted Line Chart
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
    Line Charts/Line Hollow 
    Example of Hollow Line Charts  
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
    Line Charts/Many Lines    
    Example of Multiple Line Charts
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
    
def test_bar():
    '''
    Bar Charts/Bar Chart
    Make a Bar Chart
    To add more than one set of bars to a bar chart, see [Bar Chart 2](bar_2.html)
    '''                                                                                 
    t = title(text=time.strftime('%a %Y %b %d'))
    b = bar()
    b.values = range(9,0,-1)
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(b)
    return chart
     
def test_bar_2():
    '''
    Bar Charts/Bar Chart 2
    Add more than one bar to the chart  
    '''                                                                                 
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = bar()
    b1.values = range(9,0,-1)
    b2 = bar()
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return chart
    

def test_bar_filled():
    '''
    Bar Filled Charts/Bar Filled Chart
    Set the outline colour
    '''                                                                                 
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = bar_filled(colour='#E2D66A')
    b1.values = range(9,0,-1)
    b1.outline_colour = '#577261'
    chart = open_flash_chart(bg_colour="#FFFFFF")
    chart.title = t    
    chart.add_element(b1)
    return chart

def test_horizontal_bar():
    '''
    Horizontal Bar Charts/Horizontal Bar Chart
    Make a horizontal bar chart
    '''                        
    t = title(text="Our New House Schedule")
    hb = hbar(colour="#86BBEF")
    hb.tooltip = ("Months: #val#")
    values = [ hbar_value(left=0, right=4), 
        hbar_value(left=4, right=8)]
    h3 = hbar_value(left=8, right=11)
    h3.tip = "#left# to #right#<br>%s to %s (#val# months)" % (months[8], months[11]) 
    values.append(h3)
    hb.values = values
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(hb)    
    x = x_axis()
    x.offset = False
    x.labels = labels(labels=months)
    y = y_axis()
    y.offset = 1
    y.labels = ["Make garden look sexy","Paint house","Move into house"]
    chart.x_axis = x
    chart.y_axis = y
    return chart
    
def scurve():
    i = 0.0
    data = []
    while i <=6.2:
        data.append(math.sin(i)*1.9)
        i += 0.2
    return data
    
def test_area_line():
    '''
    Area Charts/Area Line Chart
    Make an area chart.
    
    See also [Area Hollow](area_hollow.html)
    '''                                     
    t = title(text="Area Chart")
    a = area_line()
    a.width = 2
    a.dot_size = 4
    a.halo_size = 1
    a.colour = '#C4B86A'
    a.fill_colour = '#C4B8AA'
    a.fill_alpha = 0.7 
    a.values = scurve()
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(a)
    y  = y_axis()
    y.min, y.max, y.steps = -2, 2, 2
    y.labels = None
    y.offset = False
    
    x = x_axis()
    x.labels = scurve()
    x.steps = 2
    xlbls = x_axis_labels(steps=4, rotate="vertical")
    x.labels = xlbls
    
    chart.y_axis = y
    chart.x_axis = x
    return chart
    
def test_area_hollow():
    '''
    Area Charts/Area Hollow Chart
    Make an area chart.

    See also [Area Line](area_line.html)
    '''                                     
    t = title(text="Area Hollow Chart")
    a = area_hollow()
    a.width = 2
    a.dot_size = 4
    a.halo_size = 1
    a.colour = '#C4B86A'
    a.fill_colour = '#C4B8AA'
    a.fill_alpha = 0.7 
    a.values = scurve()
    chart = open_flash_chart()
    chart.title = t
    chart.add_element(a)
    y  = y_axis()
    y.min, y.max, y.steps = -2, 2, 2
    y.labels = None
    y.offset = False

    x = x_axis()
    x.labels = scurve()
    x.steps = 2
    xlbls = x_axis_labels(steps=4, rotate="vertical")
    x.labels = xlbls

    chart.y_axis = y
    chart.x_axis = x
    return chart        
    
def scircle(): 
    data = []
    for i in range(0,360,5):    
        sv = scatter_value(
            x='%.2f' % math.sin(math.radians(i)),
            y='%.2f' % math.cos(math.radians(i))
        )
        data.append(sv)
    return data
    
    
def test_scatter_chart():
    '''
    Scatter Charts/Scatter Chart
    Make a scatter chart 
    
    *Note:* The above plot should look circular but looks elliptical instead
    because the y-axis is scaled w.r.t x-axis (780:300).
    
    '''                 
    chart = open_flash_chart()
    chart.title = title(text='Scatter Chart')
    s1 = scatter(colour="#FFD600", dot_size=10)
    s1.values = [scatter_value(x=0, y=0)]
    chart.add_element(s1)
    s2 = scatter(colour="#D600FF", dot_size=3)
    s2.values = scircle()
    chart.add_element(s2)
    x = x_axis()
    y = y_axis()
    x.min, x.max, x.steps = -2, 2, 1
    y.min, y.max, y.steps = -2, 2, 1
    chart.x_axis = x
    chart.y_axis = y
    return chart
        

def test_scatter_line_chart():
    '''
    Scatter Charts/Scatter Line Chart
    Make a scatter line chart
    '''
    
    chart = open_flash_chart()
    chart.title = title(text='Scatter Line Chart')
    s = scatter_line(colour="#FFD600", dot_size=3)
    x = 0.0
    y = 0
    v = []
    while(x<25):
        v.append(scatter_value(x=x,y=y))
        y = random.randint(-20,20)/10
        if y > 10: y = 10
        if y < -10 : y = -10
        x += random.randint(5, 15)/10
    s.values = v
    chart.add_element(s)
    
    xa = x_axis()
    xa.min, xa.max = 0,25
    chart.x_axis = xa
    ya = y_axis()
    ya.min, ya.max = -10, 10
    chart.y_axis = ya
    return chart
                

def test_radar_charts_1():
    '''
    Radar Charts/Radar Chart 
    Radar Chart with filled area and value labels.
    '''                                           
    chart = open_flash_chart() 
    chart.title = title(text='Radar Chart')
    area = area_hollow()
    area.width = 1
    area.dot_size = 1
    area.halo_size = 1
    area.colour = '#45909F'
    area.fill_colour = '#45909F'
    area.fill_alpha = 0.4
    area.loop = True
    area.values = [3, 4, 5, 4, 3, 3, 2.5]
    chart.add_element(area) 
    r = radar_axis(max=5)
    r.colour ='#EFD1EF'
    r.grid_colour = '#EFD1EF'
    ra = radar_axis_labels(labels=['0','1','2','3','4','5'])
    ra.colour = '#9F819F'
    r.labels = ra
    chart.radar_axis = r
    tip = tooltip()
    tip.proximity = 1
    chart.tooltip = tip
    chart.bg_colour = '#DFFFEC'
    return chart    
    
def test_radar_charts_2():
    '''
    Radar Charts/Lines & Spoke labels
    
    Radar Chart  with lines, spoke labels and keys
    For radar charts it is neccessary to set the line style to 'loop' so the first and last points are connected. 
    In the above example you can see that the gold line has not had its loop attribute set.

    The default tooltip is of no use with radar charts so we change its behaviour to proximity.
    '''
    chart = open_flash_chart() 
    chart.title = title(text='Radar Chart')
    line1 = line_hollow()
    line1.width = 1
    line1.dot_size = 3
    line1.halo_size = 2
    line1.colour = '#FBB829'
    line1.values = [3, 4, 5, 4, 3, 3, 2.5]
    line1.tip = "Gold #val#"
    line1.text = 'Mr. Gold'
    line1.font_size = 10
    chart.add_element(line1)
    
    line2 = line_dot()
    line2.values = [2 for i in range(7)]
    line2.halo_size = 2
    line2.width = 1
    line2.dot_size = 3
    line2.colour = '#80000FF'
    line2.tip = 'Purple #val#'
    line2.text = 'Mr. Purple'
    line2.font_size = 10
    line2.loop = True
    chart.add_element(line2)
     
    r = radar_axis(max=5)
    r.colour ='#DAD5E0'
    r.grid_colour = '#DAD5E0'
    ra = radar_axis_labels(labels=['Zero','','','Middle','','High'])
    ra.colour = '#9F819F'
    r.labels = ra
    sa = radar_spoke_labels(labels=['Strength', 'Smarts', 'Sweet<br>Tooth',
            'Armour', 'Max Hit Points', '???', 'Looks Like a Monkey'])
    sa.colour = '#9F819F'
    chart.radar_axis = r 
    r.spoke_labels = sa
    tip = tooltip()
    tip.proximity = 1
    chart.tooltip = tip
    chart.bg_colour = '#FFFFFF'
    return chart
    
def test_radar_charts_3():
    '''
    Radar Charts/Stepped axis
    Radar Chart with stepped axis and custom tooltips for individual points.
    '''
    chart = open_flash_chart()
    chart.title = title(text='Radar Chart')
    
    val1 = [30,50,60,70,80,90,100,115,130,115,100,90,80,70,60,50]
    spokes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    val2 = []
    
    for i in val1:                                   
        txt = "#val#<br>Spoke: %s" % i 
        tmp = dot_value(value=i,  colour='#D41E47', tip=txt)
        val2.append(tmp)
    line = line_hollow()
    line.values = val2
    line.halo_size = 0
    line.width = 2
    line.dot_size = 6
    line.colour = '#FBB829'
    line.text = 'Hearts'
    line.font_size = 10
    line.loop = True
    chart.add_element(line)
    r = radar_axis(max=150)
    r.step = 10
    r.colour = '#DAD5E0'
    r.grid_colour = '#EFEFEF'
    chart.radar_axis = r
    tip = tooltip(proximity=1)
    chart.tooltip = tip
    chart.bg_colour = '#FFFFFF'
    return chart    
         
def test_x_axis_labels_1():
    '''
    X Axis Labels/X Axis Labels 1
    
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
	X Axis Labels/X Axis Labels 3
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


def test_shape():
    '''
    Shapes/Shapes
    Add Shapes to charts.
    '''                  
    chart = open_flash_chart()
    t = title(text="Random shape")
    chart.title = t    
    s = shape(colour="#89ad34")
    s.values = [{'x': random.randint(1,10), 'y': random.randint(1,10)} for i in range(5)]
    chart.add_element(s)        
    x = x_axis()
    x.offset = False
    x.labels = labels(labels=months)
    chart.x_axis = x                                                         
    return chart
    
    
def _test():
    test_line()
    test_line_dot()
    test_line_hollow()
    test_manylines()
    test_x_axis_labels_1()
    test_x_axis_labels_1()
    test_bar()
    
	
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
    <p>The source is available at <a href="http://github.com/btbytes/pyofc2">http://github.com/btbytes/pyofc2</a>. <br/>Use the <img src="http://assets2.github.com/images/modules/repos/download_button.png" /> button or use <code>git</code>
    <br/>
    <pre><code> $git clone git://github.com/btbytes/pyofc2.git </code></pre>   
    </p>
    <h3>Sample code</h3>
    <p> The <code>demo</code> directory has a examples.py file which illustrates how to use all the charts available in PyOFC2</p>
    <p> The see the examples, run <pre><code>$ python examples.py</code></pre></p>

    <p>which will compile all the examples and generate HTML files containing charts</p>
    <p>To see the generated charts, run <pre><code>$ ./start.sh </code></pre></p>
    ''' },
    ]
    
    
def build_examples():
    funcs = [f for f in listfunc() if f.__name__.startswith('test_')]
    examples = []
    categories = []
    for f in funcs:
        fdoc = f.__doc__.split('\n')
        cat, title = fdoc[1].strip().split('/')
        doc = markdown2.markdown('\n'.join([l.strip() for l in fdoc[2:]]))
        name = f.__name__.split('test_')[1]
        json = ''
        if f():
            json = f().render()
        code = inspect.getsource(f) 
        cstart = code.find("'''")
        cend = code.find("'''", cstart+3)+3
        code = code[:cstart]+ code[cend:]
        
        try:
            from pygments import highlight
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import HtmlFormatter

            lexer = get_lexer_by_name("python", stripall=True)
            formatter = HtmlFormatter(linenos=False, cssclass="syntax")
            code = highlight(code, lexer, formatter)
        except:
            pass 
        if cat not in categories:
            categories.append(cat)
            
        example = {
            'name': name,
            'title': title,
            'cat':cat,
            'doc': doc,
            'code': code,
            'datafile': 'data/%s.json' % (name, ),
            'json': json
            } 
        examples.append(example)
        
    #generate data files & sidebar links
    for e in examples:
        outf = open(e['datafile'], 'w')
        outf.write(e['json'])
        outf.close()     

    sidebar = '<dl>%s</dl>'
    links = []
    for cat in categories:
        links.append('<dt class="el2">%s</dt><dd>' % cat)
        for e in examples: #inefficient.. much
            if cat == e['cat']:
                links.append('<li><a href="%s">%s</a></li>' %(e['name']+'.html', e['title']))      
        links.append('</dd>')
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
    
    

