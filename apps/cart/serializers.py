from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.education.serializers import BookListSerializer
from apps.product.serializers import ProductListSerializer
from helpers.utils import update_cart

from .models import (Cart, CartItem, CartProduct, District, Order, PaymentType,
                     Region)


class CartItemCreateSerializer(ModelSerializer):
    ct_model = serializers.CharField(write_only=True)
    object_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("ct_model", "object_slug")

    def create(self, validated_data):
        try:
            content_type = ContentType.objects.get(model=validated_data["ct_model"])
            product = content_type.model_class().objects.get(slug=validated_data["object_slug"])
        except:
            raise Http404

        user = self.context["request"].user

        cart = Cart.objects.filter(user_id=user, in_order=False).first()
 
        cart_item, created = CartItem.objects.get_or_create(
            user_id=user, cart=cart, content_type=content_type, object_id=product.id
        )

        if created:
            CartProduct.objects.create(cart_id=cart, product_id=cart_item)

        update_cart(user=user, cart=cart)

        return cart_item


class ChangeCartItemQTYSerializer(ModelSerializer):
    ct_model = serializers.CharField(write_only=True)
    object_slug = serializers.SlugField(write_only=True)
    qty = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("ct_model", "object_slug", "qty")

    def create(self, validated_data):
        try:
            content_type = ContentType.objects.get(model=validated_data["ct_model"])
            product = content_type.model_class().objects.get(slug=validated_data["object_slug"])
        except:
            raise Http404

        user = self.context["request"].user

        cart = Cart.objects.filter(user_id=user, in_order=False).first()

        cart_item = CartItem.objects.get(user_id=user, cart=cart, content_type=content_type, object_id=product.id)
        cart_item.qty = validated_data["qty"]
        cart_item.save()

        update_cart(user=user, cart=cart)

        return cart_item


class CartItemDeleteFromCartSerializer(ModelSerializer):
    ct_model = serializers.CharField(write_only=True)
    object_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("ct_model", "object_slug", "cart_id")

    def create(self, validated_data):
        user = self.context["request"].user

        try:
            content_type = ContentType.objects.get(model=validated_data["ct_model"])
            product = content_type.model_class().objects.get(slug=validated_data["object_slug"])
            cart = Cart.objects.get(user_id=user, in_order=False)
        except:
            raise Http404

        cart_item = CartItem.objects.get(user_id=user, cart=cart, content_type=content_type, object_id=product.id)
        cart_item.delete()

        update_cart(user=user, cart=cart)

        return cart_item


class CartItemListSerializer(ModelSerializer):
    product_data = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = (
            "content_type",
            "object_id",
            "product_data",
            "qty",
            "final_price",
        )

    def get_product_data(self, obj):
        if obj.content_type_id == 21:
            serializer = BookListSerializer(obj.content_object, context={"request": self.context["request"]})
        elif obj.content_type_id == 23:
            serializer = ProductListSerializer(obj.content_object, context={"request": self.context["request"]})
        else:
            return {}
        return serializer.data


class CartDetailSerializer(ModelSerializer):
    user_id = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ("id", "user_id", "total_products", "final_price")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        products = CartItem.objects.filter(cart=instance)

        if products.exists():
            serializer = CartItemListSerializer(products, many=True, context={"request": self.context["request"]})
            representation["products"] = serializer.data

        return representation


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "cart_id",
            "first_name",
            "last_name",
            "phone_number",
            "buying_type",
            "region_id",
            "district_id",
            "home_address",
            "text",
            "payment_type",
        )

        read_only_fields = ("user_id",)

    def create(self, validated_data):
        cart_id = validated_data["cart_id"]
        cart = Cart.objects.get(id=cart_id.id)
        if cart.in_order != False:
            raise serializers.ValidationError({"message": "Bu savatga buyurtma berilgan!"})

        cart.in_order = True
        cart.save()

        user = self.context["request"].user
        Cart.objects.create(user_id=user, in_order=False)

        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["order_number"] = instance.order_number

        return representation


class RegionListSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "title")


class DistrictListSerializer(ModelSerializer):
    region_id = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ("id", "title", "region_id")


class PaymentTypeListSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ("id", "title")


class CartMiniForOrderListSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ("id", "final_price")

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        products = CartItem.objects.filter(cart=instance)

        if products.exists():
            serializer = CartItemListSerializer(products, many=True, context={"request": self.context["request"]})
            representation["products"] = serializer.data

        return representation


class OrderListSerializer(ModelSerializer):
    cart_id = CartMiniForOrderListSerializer()

    class Meta:
        model = Order
        fields = ("id", "order_number", "status", "cart_id")
