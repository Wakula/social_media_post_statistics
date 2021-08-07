from post_statistics import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post_statistics', views.PostStatisticsViewSet, 'post-statistics')


urlpatterns = [
    *router.urls
]
