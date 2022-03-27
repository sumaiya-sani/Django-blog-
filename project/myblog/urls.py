
from unicodedata import name
from django.urls import path
from.views import *
from myblog import views

app_name='myblog'

urlpatterns = [
   # path('home/',views.home,name='home'),
   path('home/',homeview.as_view(), name="home"),
   path('article/<int:pk>',ArticleDetailView.as_view(),name="article_detail"),
   path('create_post/',AddPostView.as_view(),name="add_post"),
   path('add_category/',AddCategoryView.as_view(),name="add_category"),
   path('artical/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
   path('artical/remove/<int:pk>',DeletePostView.as_view(),name="delete_post"),
   path('category/<str:cats>/',views.categoryView,name="category_page"),
   path('like/<int:pk>',LikeView,name='like_post'),
   path('artical/<int:pk>/comment',AddCommentView.as_view(),name="add_comment"),




]
