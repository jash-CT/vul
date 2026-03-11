from django.urls import path
from .views import PaymentViewSet, SubscriptionViewSet

urlpatterns = [
    path('payments/', PaymentViewSet.as_view(), name='payments'),
    path('subscriptions/', SubscriptionViewSet.as_view(), name='subscriptions'),
]