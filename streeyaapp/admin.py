from django.contrib import admin

# Register your models here.
from .models import *

# from .models import Review
# from .models import sub_cat_item


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
admin.site.register(StaffProfile)





