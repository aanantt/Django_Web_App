"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from post import views as post_views
from samplelogin import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.register, name='signup'),
    path('user/follow/<int:user_id>/', user_views.followerhandler, name='followsystem'),
    path('user/<int:user_id>/', user_views.userhome, name='userhome'),
    path('user/profile/', user_views.image, name='userimage'),
    path('login/', auth_views.LoginView.as_view(template_name='samplelogin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='samplelogin/logout.html'), name='logout'),
    path('', post_views.PostListView.as_view(), name="home"),
    path('post/like/<int:post_id>/', post_views.like_disliked, name="like-disliked"),
    path('detail/<int:post_id>/', post_views.detail_view, name="post-detail"),
    path('search/', post_views.search, name="post-search"),
    path('post/new/', post_views.PostCreateView.as_view(), name="post-create"),
    path('post/comment/delete/<int:pk>/<int:c>', post_views.delete_comment, name="comment-delete"),
    path('post/comment/<int:post_id>/', post_views.load, name="post-comment"),
    path('user/', user_views.userr, name="current-user"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)