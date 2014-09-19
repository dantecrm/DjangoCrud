from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'crud.views.inicio', name="inicio"),
    url(r'^agregar/$', 'crud.views.agregar', name="agregar"),
    url(r'^editar/(?P<id>\d+)$', 'crud.views.editar', name="editar"),
    url(r'^borrar/(?P<id>\d+)$', 'crud.views.borrar', name="borrar"),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
