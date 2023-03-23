from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from helpers.utils import update_cart

from .models import Cart, CartItem, CartProduct


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

        cart_item = CartItem.objects.filter(user_id=user, cart=cart, content_type=content_type, object_id=product.id)

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


class CartDetailSerializer(ModelSerializer):
    user_id = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ("user_id", "total_products", "final_price")
