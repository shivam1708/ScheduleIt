from django.conf.urls import url
from app import views

# SET THE NAMESPACE!
app_name = 'app'


urlpatterns=[
    url(r'^add/$',views.student_add,name='student_add'),
    url(r'^remove/$',views.student_remove,name='student_remove'),
    url(r'^subscribed/$',views.subscribed,name='subscribed'),
    url(r'^register/$',views.register,name='register'),
    url(r'^unregister/$',views.unregister,name='unregister'),
    url(r'^registerevent/$',views.registerevent,name='registerevent'),
    url(r'^admin/user_login/$',views.admin_user_login,name='admin_user_login'),
    url(r'^admin/user_logout/$', views.admin_user_logout, name='admin_user_logout'),
    url(r'^admin/(?P<id>[\w-]+)/$',views.admin_fire,name='admin_fire'),
    url(r'^student/$',views.student,name='student'),
    url(r'^student/register/$',views.student_register,name='student_register'),
    url(r'^student/user_login/$',views.student_user_login,name='student_user_login'),
    url(r'^student/user_logout/$', views.student_user_logout, name='student_user_logout'),
    url(r'^student/(?P<id>[\w-]+)/$',views.student_fire,name='student_fire'),
    url(r'^showsub/$',views.student_showsub,name='student_showsub'),
    url(r'^enter/$',views.student_enter,name='student_enter'),
    url(r'^browse/$',views.student_browse,name='student_browse'),
    #url(r'^council/$',views.council,name='council'),
    url(r'^council/register/$',views.council_register,name='council_register'),
    url(r'^council/user_login/$',views.council_user_login,name='council_user_login'),
    url(r'^council/user_logout/$', views.council_user_logout, name='council_user_logout'),
    url(r'^council/(?P<id>[\w-]+)/$',views.council_fire,name='council_fire'),
    # url(r'^admin/$',views.student,name='student'),
    # url(r'^admin/register/$',views.register,name='register'),
]
