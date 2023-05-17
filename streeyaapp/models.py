from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.forms import NullBooleanField
# Create your models here.
# Admin side elements
class Category(models.Model):
    category = models.CharField(max_length=16)

    def __str__(self):
        return self.category

class SubCategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_cat')
    sub_category = models.CharField(max_length=16)
    sub_category_code = models.CharField(max_length=5)

    def __str__(self):
        return self.sub_category

class Type(models.Model):
    types = models.CharField(max_length=25)
    type_code = models.CharField(max_length=5)

    def __str__(self):
        return self.types

class TrendingProduct(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class HotRightNow(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class HotRightNowMobile(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items


class DealYouDontMiss(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class OfferPoster(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class OfferPosterMobile(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class BannerImage(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class BannerImageMobile(models.Model):
    img = models.ImageField(upload_to="media")
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class CircularBanner(models.Model):
    img = models.ImageField(upload_to="media")
    name = models.CharField(max_length=16)
    related_items = models.CharField(max_length=20)

    def __str__(self):
        return self.related_items

class Details(models.Model):
    details_name = models.CharField(max_length=100)
    details_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.details_name
    
class ProductId(models.Model):
    product_id = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.product_id
    

    
class Item(models.Model):
    item_unique_id = models.CharField(max_length=16, unique = True)
    name = models.CharField(max_length=150)
    item_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='item_of_type')
    sub_cat_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='item_of_subcat')
    product_code = models.ForeignKey(ProductId, on_delete=models.CASCADE, related_name='item_of_product_id')
    original_price = models.IntegerField()
    offer_price = models.IntegerField()
    description = models.TextField()
    sticker_value = models.CharField(max_length=150, default=None)
    available = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_unique_id

class ItemDetail(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='detail')
    detail_id = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='item_detail')
    details_info = models.CharField(max_length=100)

    def __str__(self):
        return self.item_id.item_unique_id



# class Review(models.Model):
#     item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='revw')
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rev')
#     rating = models.IntegerField()
#     review = models.TextField()

#     def __str__(self):
#         return self.item_id.item_unique_id


class Image(models.Model):
    img = models.ImageField(upload_to="media")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='img')

    def __str__(self):
        return self.item_id.item_unique_id

class ItemTrend(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='trend')
    img_id = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='img_trend')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id.item_unique_id


class SizeChart(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.size

class ItemSize(models.Model):
    item_unique_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='avail_size')
    size_id = models.ForeignKey(SizeChart, on_delete=models.CASCADE)
    number_of_item = models.IntegerField()
    avail = models.BooleanField(default=False)

    def __str__(self):
        return self.item_unique_id.item_unique_id

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_trend_id = models.ForeignKey(ItemTrend, on_delete=models.CASCADE)
    item_size = models.ForeignKey(ItemSize, on_delete=models.CASCADE)
    item_qty = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_trend_id = models.ForeignKey(ItemTrend, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Coupon codes

class DiscountPercentage(models.Model):
    discount_percent = models.IntegerField()

    def __str__(self):
        return str(self.discount_percent)

class CouponCode(models.Model):
    code = models.CharField(max_length=8,unique = True)
    code_generated_by = models.OneToOneField(User, on_delete=models.CASCADE)
    code_generated_for = models.CharField(max_length=50)
    code_owner_passcode = models.CharField(max_length=16, unique = True)
    code_desc = models.TextField()
    discount = models.ForeignKey(DiscountPercentage, on_delete=models.CASCADE)
    code_avail_count = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class CouponUsed(models.Model):
    code = models.ForeignKey(CouponCode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    used_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code.code


# Selling details

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)
    house_no = models.TextField()
    area = models.TextField()
    contact = models.CharField(max_length=15)
    alternet_contact = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return self.pin_code
        
class PaymentMethod(models.Model):
    methods = models.CharField(max_length=30)

    def __str__(self):
        return self.methods

class Order(models.Model):
    order_id = models.CharField(max_length=16, unique = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='address')
    ordered_on = models.DateTimeField(auto_now_add=True)
    pament_amount = models.IntegerField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='payment_order')

    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):
    item_uid = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_detail')
    order_uid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    order_item_size = models.ForeignKey(SizeChart, on_delete=models.CASCADE, related_name='item_siz')

    def __str__(self):
        return self.order_uid.order_id
    
class OrderStatus(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_status')
    shipped = models.BooleanField(default=False)
    shipped_on = models.DateTimeField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    paid_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.order_id.order_number
    
class Complaint(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_related')
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_number')
    compl_desc = models.TextField()

class StaffProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media")
    staff_id = models.CharField(max_length=16)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)
    area = models.TextField()
    contact = models.CharField(max_length=15)
    alternet_contact = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name






