from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books/add$', views.add_book),
    url(r'^book_being_added$', views.book_being_added),
    url(r'^delete_review/(?P<book_id>\d+)/(?P<review_id>\d+)$', views.delete_review),
    url(r'^review_being_added/(?P<book_id>\d+)$', views.review_being_added),
    url(r'^logout$', views.logout,),
    url(r'^books/(?P<book_id>\d+)$', views.one_book_page),
    url(r'^users/(?P<user_id>\d+)$', views.user_profile)
]