from rest_framework.routers import DefaultRouter
from django.urls import path, include
from posts.views import PostViewSet, AuthorViewSet, TagViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('authors', AuthorViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]



# from posts.views import PostView, TagView, TagDetailView, AuthorView, AuthorDetailView, PostDetailView


# urlpatterns = [
#     path("", PostView.as_view()),
#     path("<int:pk>/", PostDetailView.as_view()),
#     path("tags/", TagView.as_view()),
#     path("tags/<int:pk>/", TagView.as_view()),
#     path("authors/", AuthorView.as_view()),
#     path("authors/<int:pk>/", AuthorDetailView.as_view()),
# ]
