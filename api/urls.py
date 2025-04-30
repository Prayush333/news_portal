from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'catagory',views.CategoryViewSet)
router.register(r'tag',views.TagViewSet)
router.register(r'post',views.PostViewSet)
router.register(r'contact',views.ContactViewSet)
router.register(r'newsletter',views.NewsletterViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("post-by-category/<int:category_id>/",views.PostListByCategoryView.as_view(), name="post-by-category"),
    path(
        "draft-list/",
        views.DraftListView.as_view(),
        name="draft-list-api",
    ), 

      path(
        "draft-detail/<int:pk>",
        views.DraftDetailView.as_view(),
        name="draft-detail-api",
    ), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]