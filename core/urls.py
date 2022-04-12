from django.urls import path, include

from .views import (
    HomeView,
    CategoryDetailView,
    CartDetailView,
    CheckoutDetailView,
    CustomerProfileView,

    product_detail_view,
    cart_detail_view,

    #  Article views
    ArticleListView,
    article_detail_view,

    InstallProssecc,
    AdminControlPanel,
    request_completed,
    request_uncompleted,
    accessory_tool_detail_view,

    # SearchResultsView,
    search_query,
)

app_name='Core'

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    
    path('category/<slug:slug_category>/', CategoryDetailView.as_view(), name='category-detail-view'),
    path('category/<slug:slug_category>/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail-view'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('ajax/search_query/', search_query, name='search_query'),


    path('cart/', CartDetailView.as_view(), name='cart-detail-view'),
    path('profile/', CustomerProfileView.as_view(), name='customer-profile-view'),
    path('checkout/', CheckoutDetailView.as_view(), name='checkout-detail-view'),

    path('ajax/detail/', product_detail_view, name='product_detail_view'),
    path('ajax/cart/detail/', cart_detail_view, name='cart_detail_view'),


    path('article/', ArticleListView.as_view(), name='article-veiw'),
    path('ajax/article_detail_view/', article_detail_view, name='article_detail_view'),

    path('install-prossecc/', InstallProssecc.as_view(), name='install-view'),
    path('admin-panel/', AdminControlPanel.as_view(), name='admin-veiw'),
    path('admin-panel/<int:pk>/', AdminControlPanel.as_view(), name='admin-veiw'),
    path('ajax/request_completed/', request_completed, name='request_completed'),
    path('ajax/request_uncompleted/', request_uncompleted, name='request_uncompleted'),
    path('ajax/accessory_tool_detail_view/', accessory_tool_detail_view, name='accessory_tool_detail_view'),
]
