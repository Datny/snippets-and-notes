
@@@@@@@@@@@ This file is in BASEDIR + templatetags directory with another file "__init__.py"  , init is just empty file
@@@@@@@@@@@ 
my_filter.py contains: 

	from django import template

	register =  template.Library()

	@register.filter(name="cutz")
	def cutts(value,arg):
	    """This cuts out all vlaues of "arg" from string """
	    return value.replace(arg, '')


	#register.filter('cutz', cutts)

@@@@@@@@@@
@@@@@@@@@@ How to implement in any html file,  important lines have >> sign 

	<!DOCTYPE html>
	{% extends "basic_app/base.html" %}
>>>>>>>>>>> {% load my_filter %}

	    {% block body_block %}
>>>>>>>>>>> <h1>{{ text|cutz:'hello'}}</h1>
	    <h1>{{ number|add:"99" }}</h1>
	    {% endblock %}
