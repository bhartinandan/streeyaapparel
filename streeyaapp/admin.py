from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Category
from .models import SubCategory
from .models import Type
from .models import TrendingProduct
from .models import HotRightNow
from .models import HotRightNowMobile
from .models import DealYouDontMiss
from .models import OfferPoster
from .models import OfferPosterMobile
from .models import BannerImage
from .models import BannerImageMobile
from .models import CircularBanner
from .models import Details
from .models import ProductId
from .models import Item, ItemDetail
from .models import Image
from .models import ItemTrend
from .models import SizeChart
from .models import ItemSize
from .models import Cart
from .models import DiscountPercentage
from .models import CouponCode
from .models import CouponUsed
from .models import Address
from .models import PaymentMethod
from .models import Order
from .models import OrderStatus
from .models import Complaint








# from .models import Review
# from .models import sub_cat_item









from .models import TrendingProduct
from .models import ItemDetail


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Type)
admin.site.register(TrendingProduct)
admin.site.register(HotRightNow)
admin.site.register(HotRightNowMobile)
admin.site.register(DealYouDontMiss)
admin.site.register(OfferPoster)
admin.site.register(OfferPosterMobile)
admin.site.register(BannerImage)
admin.site.register(BannerImageMobile)
admin.site.register(CircularBanner)
admin.site.register(Details)
admin.site.register(ProductId)
admin.site.register(Item)
admin.site.register(ItemDetail)
admin.site.register(Image)
admin.site.register(ItemTrend)
admin.site.register(SizeChart)
admin.site.register(ItemSize)
admin.site.register(Cart)
admin.site.register(DiscountPercentage)
admin.site.register(CouponCode)
admin.site.register(CouponUsed)
admin.site.register(Address)
admin.site.register(PaymentMethod)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Complaint)





