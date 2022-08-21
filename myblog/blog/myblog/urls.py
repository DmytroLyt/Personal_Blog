from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, CategoryListView, LikeView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),

]
