from django.contrib import admin
from django.urls import path,include
from streeyaapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.index, name='index'),
    path("userlogin",views.userlogin, name='userlogin'),
    path("userlogout",views.userlogout, name='logout'),
    path("usersignup",views.usersignup, name='signup'),
    path("enterotp",views.enterotp, name='enterotp'),
    path("enterpassword",views.enterpassword, name='enterpassword'),
    path("product",views.product, name='product'),
    path("search",views.selective_product, name='search'),
    path("wishlist",views.wishlist, name='wishlist'),
    path("aboutus",views.aboutus, name='aboutus'),
    path("myorder",views.myorder, name='myorder'),
    path("trackorder",views.track_order, name='trackorder'),
    path("cancelorder",views.cancelorder, name='cancelorder'),
    path("chooseaddress",views.chooseaddress, name='chooseadd'),
    path("editaddress/<id>",views.edit_address, name='editaddress'),
    path("deleteaddress/<id>",views.deleteaddress, name='deleteaddress'),
    path("product-detail/<id>/<str:nam>",views.product_def, name='product_detail'),
    #--------------------------------------------
    path("logout",views.logout, name='logout'),
    path("dashboard",views.dashboard, name='dashboard'),
    path("add_data",views.add_data, name='add_data'),
    path("adddatadetail/<id>",views.add_detail, name='add_data_detail'),
    path("deldatadetail/<int:id>/<int:id2>",views.del_detail, name='del_data_detail'),
    path("order_detail",views.order_detail, name='ord_det'),
    path("coupon_code",views.coupon_code, name='coup_det'),
    path("stafflogin",views.stafflogin, name='staffln'),
    path('stafflogout', views.stafflogout,name="stafflogout"),
    path("dispatched",views.order_detail_dispatched, name='ord_dispatched'),
    path("delivered",views.order_detail_delivered, name='ord_delivered'),
    path('clickposter/<str:poster_value>', views.poster_to_product, name='poster_to_product'),
    # path("print_address/<id>",views.print_address, name='print_add'),
    path("dispatch/<id>",views.dispatch, name='dispatch'),
    path("deliver/<id>",views.deliver, name='deliver'),
    path("addposter",views.add_poster, name='addposter'),
    path("addmobbanner/<id>",views.mob_view_banner, name='mobviwban'),
    path("replacebanner/<id>",views.replace_banner, name='addban'),
    path("replace-mobile-banner/<id>",views.replace_mbanner, name='replace-mobile-banner'),
    path("product",views.product, name='product_page'),
    path("addcb",views.add_circular_banner, name='addcb'),
    path("delcb/<id>",views.del_circular_banner, name='delcb'),
    path("addtp",views.add_trending_product, name='addtp'),
    path("deltp/<id>",views.del_trending_product, name='deltp'),
    path("hot/<id>",views.replace_hot, name='hot'),
    path("mhot/<id>",views.replace_mhot, name='mhot'),
    path("adddeal",views.add_deal_dont_wanna_miss, name='addcb'),
    path("deldeal/<id>",views.del_deal_dont_wanna_miss, name='delcb'),
    path("offerpos/<id>",views.offer_poster, name='offerpos'),
    path("offermpos/<id>",views.offer_mposter, name='offermpos'),
    path("updateitem",views.update_item, name='updatedata'),
    path("cart",views.cart, name='cart'),
    path("delcartitem/<id>",views.delcartitem, name='delcart'),
    path("addcart/<id>",views.addcart, name='addcart'),
    path("payment",views.payment, name='payment'),
    path("viewimg/<id>",views.view_item_image, name='viewimg'),
    path("updateimg/<id>",views.update_img, name='updateimg'),
    
    
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)