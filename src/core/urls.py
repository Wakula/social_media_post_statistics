from django.urls import path, include

urlpatterns = [
    path('api/statistics_service/', include('post_statistics.urls')),
]
