from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from gid import views
from gid.views import login, register, index, logout, catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('catalog/', catalog, name='catalog'),
    path('sight/<int:sight_id>/', views.sight_detail, name='sight_detail'),
    path('sight/<int:sight_id>/comment_submit/', views.submit_comment, name='comment_submit'),
    path('sight/<int:sight_id>/mark_visited/', views.mark_visited, name='mark_visited'),
    path('visited_sights/', views.user_visited_sights, name='user_visited_sights'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
