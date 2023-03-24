from django.urls import path
from .views import ProductViewSet, LikeView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        # 'post': 'create'
    })),
    path('products/<uuid:pk>/like', LikeView.as_view())
]