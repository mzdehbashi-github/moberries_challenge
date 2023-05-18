from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from pizza.models.order_result import OrderResult
from pizza.serializers.v1.order_result import OrderResultSerializer


class OrderResultView(GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = OrderResult.objects.all()
    serializer_class = OrderResultSerializer
