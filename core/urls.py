from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

schema_view = get_schema_view(
    openapi.Info(
        title="UzChess API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # swagger
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    # apps
    path("api/cart/", include("apps.cart.urls")),
    path("api/education/", include("apps.education.urls")),
    path("api/main/", include("apps.main.urls")),
    path("api/product/", include("apps.product.urls")),
    path("api/user/", include("apps.user.urls")),
    path("api/news/", include("apps.news.urls")),
)
