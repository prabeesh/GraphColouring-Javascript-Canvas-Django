from django.conf.urls.defaults import *
from graph.views import mainpage

urlpatterns = patterns('', 
    ('^$', mainpage),
)
