from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api.views import UserRegistrationViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()

router.register(r'registration', UserRegistrationViewSet, basename='registration_users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]

