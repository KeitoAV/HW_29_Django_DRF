from django.db.models import Q, Count
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from ads.models.ad import Ad
from ads.serializers.ad import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroySerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-price')

        categories = request.GET.getlist('cat', None)
        if categories:
            self.queryset = self.queryset.filter(category__id__in=categories)

        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location', None)
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(self, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES.get("image", None)
        ad.save()
        response = AdDetailSerializer(ad).data

        return JsonResponse(response)
