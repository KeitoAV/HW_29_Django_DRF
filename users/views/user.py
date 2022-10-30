
from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models.user import User
from users.serializers.user import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        published_ads = Count('ad', filter=Q(ad__is_published=True))

        self.queryset = self.queryset.prefetch_related('location').order_by('username').annotate(
            total_ads=published_ads)

        return super().get(request, *args, **kwargs)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        published_ads = Count('ad', filter=Q(ad__is_published=True))

        self.queryset = self.queryset.prefetch_related('location').order_by('username').annotate(
            total_ads=published_ads)

        return super().get(request, *args, **kwargs)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
