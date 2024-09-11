from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('addtag/', views.addtag, name='addtag'),
    path('category/<slug:slug>/', views.category_view, name='categoryview'),
    path('categories/', views.cat_list, name='category'),
    path('jquery/', views.jquery, name='jquery'),
    path('tags/<slug:slug>/', views.tag_view, name='tagview'),
    path('tags/', views.tag_list, name='tags'),

    path('post/<slug:slug>/', views.commentsection, name='comments'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name = 'signup'),
    path('user_detail', views.user_detail, name='user_detail'),
    path('user_edit', views.user_edit, name='user_edit'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)