from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

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

        cart_item = CartItem.objects.create(user_id=user, cart=cart, content_type=content_type, object_id=product.id)

        CartProduct.objects.create(cart_id=cart, product_id=cart_item)

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
        # CartProduct.objects.create(cart_id=cart, product_id=cart_item)

        return cart_item
