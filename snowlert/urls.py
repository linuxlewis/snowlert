from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from alerts import views
from stations import views as sviews

router = DefaultRouter()
router.register('stations', sviews.StationViewSet)
router.register('alerts', views.AlertViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snowlert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'alerts.views.home', name='home'),
    url(r'^stations/map/', 'stations.views.map_view', name='stations_map'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
