from django.conf.urls import url

from anims import views
# from ip import views

urlpatterns = [
    
    url(r'^$', views.index, name='ip_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='ip_index'),
    
    # 20181010_084804
    url(r'^anims/$', views.anims, name='anims'),
    
    # 20181010_120542
    url(r'^anims_JS/$', views.anims_JS, name='anims_JS'),
    
    # 20181013_071822
    url(r'^open_dir/$', views.open_dir, name='open_dir'),
    
]
