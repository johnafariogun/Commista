from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import Category, FavoriteProduct, Product
from store.serializers import ProductSerializer


# Create your views here.

class CategoryAndSalesView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get(self, request):
        categories = Category.objects.values('id', 'title')
        products_without_flash_sales = Product.categorized.filter(flash_sale_start_date=None, flash_sale_end_date=None)
        flash_sales = Product.categorized.filter(flash_sale_start_date__lte=timezone.now(),
                                                 flash_sale_end_date__gte=timezone.now())
        serializer = self.serializer_class(many=True)
        mega_sales = products_without_flash_sales.filter(percentage_off__gte=24)
        products_without_flash_sales_data = serializer.to_representation(products_without_flash_sales)
        flash_sales_data = serializer.to_representation(flash_sales)
        mega_sales_data = serializer.to_representation(mega_sales)

        data = {'categories': categories, 'product_without_flash_sales': products_without_flash_sales_data,
                'flash_sales': flash_sales_data, 'mega_sales': mega_sales_data}
        return Response({"message": "Fetched all products", "data": data, "status": "success"},
                        status=status.HTTP_200_OK)


class FavoriteProductsView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user is None:
            return Response({"message": "User does not exist", "status": "failed"}, status=status.HTTP_400_BAD_REQUEST)
        favorite_products = FavoriteProduct.objects.filter(customer=user)

        data = [
            {
                "title": product.title,
                "slug": product.slug,
                "category": product.category.name,
                "description": product.description,
                "style": product.style,
                "price": product.price,
                "percentage_off": product.percentage_off,
                "size": product.size.values_list("name", flat=True),
                "colour": product.colour.values_list("name", flat=True),
                "ratings": product.ratings,
                "inventory": product.inventory,
                "flash_sale_start_date": product.flash_sale_start_date,
                "flash_sale_end_date": product.flash_sale_end_date,
                "condition": product.condition,
                "location": product.location.name,
                "discount_price": product.discount_price,
                "average_ratings": product.average_ratings,
                "images": [image.image_url for image in product.images.all()]
            } for product in favorite_products.all()
        ]
        return Response({"message": "All favorite products fetched", "data": data, "status": "success"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"message": "Product id is required", "status": "failed"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Invalid product id", "status": "failed"},
                            status=status.HTTP_400_BAD_REQUEST)

        favorite, created = FavoriteProduct.objects.get_or_create(customer=user, product=product)

        if created:
            return Response({"message": "Product added to favorites", "status": "success"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Product already in favorites", "status": "success"}, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"message": "Product id is required", "status": "failed"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Invalid product id", "status": "failed"},
                            status=status.HTTP_400_BAD_REQUEST)

        FavoriteProduct.objects.filter(customer=user, product=product).delete()
        return Response({"message": "Product removed from favorite list", "status": "succeed"},
                        status=status.HTTP_200_OK)
