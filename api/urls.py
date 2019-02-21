from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    url(r'^ubicsubmit/$', CreateView.as_view(), name="create"),
    url(r'^ubicaciones/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="ubicaciones"),

}

urlpatterns = format_suffix_patterns(urlpatterns)