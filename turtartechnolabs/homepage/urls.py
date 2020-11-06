from django.urls import path
from homepage.views import index,about,skills,contact,blog,post

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('skills',skills,name='skills'),
    path('contact', contact,name='contact'),
    path('blog',blog,name='blog'),
    path('post/<int:sno>',post,name='post'),
  
    
    
]
