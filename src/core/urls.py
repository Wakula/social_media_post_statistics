from django.urls import path, include

urlpatterns = [
    path('api/', include('post_statistics.urls')),
]
