from django.urls import path

from newspaper import views

urlpatterns = [
    path("",views.HomeView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-by-category/<int:category_id>/", views.PostByCategoryView.as_view(), name="post-by-category"),
    path("tag-list/",views.TagListView.as_view(), name="tag-list"),
    path("about-us/",views.AboutUsView.as_view(),name="about-us"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("category-list/", views.CategoryListView.as_view(), name="category-list"),
    path("post-detail/<int:pk>/",views.PostDetailView.as_view(),name="post-detail"),
     path("tag-detail/<int:pk>/",views.TagDetailView.as_view(),name="tag-detail"),
]