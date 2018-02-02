from django.http import Http404
from rest_framework import routers, serializers, viewsets, filters

from .models import Transaction, ScheduledPayment

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Return only objects owned by the current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner_id=request.user.id)

class IsCustomerFilterBackend(filters.BaseFilterBackend):
    """
    Return only objects owned by the current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(customer__owner_id=request.user.id)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        ordering = ('-created_date',)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_date')
    serializer_class = TransactionSerializer

    filter_backends = (IsOwnerFilterBackend,)


class ScheduledPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPayment
        fields = '__all__'
        ordering = ('-created_date',)

class ScheduledPaymentViewSet(viewsets.ModelViewSet):
    queryset = ScheduledPayment.objects.all().order_by('-created_date')
    serializer_class = ScheduledPaymentSerializer
    filter_backends = (IsCustomerFilterBackend,)


router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'scheduled-payments', ScheduledPaymentViewSet)
