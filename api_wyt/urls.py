from django.conf.urls import url
from api_wyt import views

urlpatterns = [
	url(r'^wyt_content/$',views.thought_list),
]
