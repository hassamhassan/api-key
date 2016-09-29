from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from signup import views

urlpatterns = [
    url(r'^signup/$', views.SignUpList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
