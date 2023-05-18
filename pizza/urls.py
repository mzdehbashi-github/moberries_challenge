from rest_framework import routers


from pizza.views import v1


router = routers.SimpleRouter()
router.register(r'v1/pizza-order-basket', v1.PizzaOrderBasketView)
router.register(r'v1/pizza-order-item', v1.PizzaOrderItemView)
router.register(r'v1/order-result', v1.OrderResultView)
urlpatterns = router.urls
