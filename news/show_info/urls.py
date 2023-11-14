from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('news/<str:category>/', views.category_page, name='category_page'),
    path('post/<slug:post_slug>/', views.show_post, name='show_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
