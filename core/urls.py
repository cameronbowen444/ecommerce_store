from django.urls import path
from .views import HomeView, ItemDetailView, OrderSummaryView, add_to_cart, remove_from_cart, remove_single_item_from_cart, CheckoutView, PaymentView, AddCouponView, ProductsView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products', ProductsView.as_view(), name='products'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('add-coupon', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('remove_single_item_from_cart/<slug>', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment')
]
