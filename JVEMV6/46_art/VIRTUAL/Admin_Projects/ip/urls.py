from django.conf.urls import url

from ip import views

urlpatterns = [
    
    url(r'^$', views.index, name='ip_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='ip_index'),
    
    url(r'^basics/$', views.basics, name='ip_basics'),
    
    #test
    url(r'^test/$', views.test, name='ip_test'),
    
    url(r'^get_4_corners/$', views.get_4_corners, name='get_4_corners'),
    
    url(r'^open_image_dir/$', views.open_image_dir, name='open_image_dir'),
    
    url(r'^exec_get_4_corners/$', views.exec_get_4_corners, name='exec_get_4_corners'),
    
    url(r'^gen_Cake_CSV/$', views.gen_Cake_CSV, name='gen_Cake_CSV'),
    
    url(r'^dos_attack/$', views.dos_attack, name='dos_attack'),
    
    url(r'^ip_ops/$', views.ip_ops, name='ip_ops'),
    
    # 20180925_064955
    url(r'^prep_gen_Cake_CSV/$', views.prep_gen_Cake_CSV, name='prep_gen_Cake_CSV'),
    
    # 20181010_084804
    url(r'^anims/$', views.anims, name='anims'),
    
    # 20181010_120542
    url(r'^anims_JS/$', views.anims_JS, name='anims_JS'),
    
    # 20181013_071822
    url(r'^open_dir/$', views.open_dir, name='open_dir'),
    
]
