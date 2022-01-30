from django.conf import settings
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.add_file, name='upload'),
    path('create/', views.create, name='create'),
    path('notes/', views.notes, name='notes'),
    path('certificates/', views.certificates, name='certificates'),
    path('documents/', views.documents, name='documents'),
    path('papers/', views.papers, name='papers'),
    path('material/', views.material, name='material'),
    path('account/', views.account, name='account'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
