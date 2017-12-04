from django.conf.urls import include, url
from django.contrib import admin

from notes.views import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.categories_view, name='categories'),
    url(r'^category/(\d+)/$', views.notes_view, name='notes'),
    url(r'^note/(\d+)/$', views.note_view, name='note'),

]
