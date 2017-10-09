from django.conf.urls import url, include

from apps.app_gestor_usuarios.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^signup/', signup),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^menu/', menu),
    url(r'^addcontact/', addcontact),
    url(r'^editcontact/', editcontact),
    url(r'^editdone/', editdone),
    url(r'^deletecontact/', deletecontact),

]
