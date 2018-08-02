from django.conf.urls import url
from new import views
from django.contrib.auth.views import login,logout

urlpatterns=[
	 url(r'^login/$', login, {'template_name':'new/login1.html'}),
	 url(r'^logout/$', logout, {'template_name':'new/logout.html'}),
	 url(r'^register/$',views.register, name="register"),
	 url(r'^profile/$',views.view_profile, name="view_profile"),
	 url(r'^profile/(?P<pk>\d+)/$',views.view_profile, name="view_profile_with_pk"),
	 url(r'^profile/edit/$',views.edit_profile, name="edit_profile"),
	 url(r'^profile/change_password/$',views.change_password, name="edit_profile")
]
