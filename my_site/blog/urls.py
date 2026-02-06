from django.urls import path
from . import views

urlpatterns = [
    # path("", views.start_page, name="home"),
    path("", views.StartingPageView.as_view(), name="home"),
    # path("posts", views.posts, name="posts_list"),
    path("posts", views.AllPostsView.as_view(), name="posts_list"),
    # path("posts/<slug:slug>", views.post_detail, name="post_detail")
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_detail")
]