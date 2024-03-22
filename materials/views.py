from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import Payment, Subscriptions
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer, PaymentSerializer, PaymentCreateSerializers, \
    SubscriptionCourseSerializers
from .services import get_pay


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'user', 'payment_method',)
    ordering_fields = ('payment_date',)


class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializers
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount_payment = serializer.validated_data.get('amount')
        method_payment = serializer.validated_data.get('payment_method_choices')

        user = self.request.user
        payment = get_pay(amount_payment, user)
        response_data = {
            "id": payment.id,
            "amount": payment.amount_payment,
            "payment_method_choices": method_payment,
            "stripe_id": payment.stripe_id
        }
        return Response(response_data)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionCourseSerializers
    queryset = Subscriptions.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionUpdateView(generics.UpdateAPIView):
    serializer_class = SubscriptionCourseSerializers
    queryset = Subscriptions.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionDestroyAPIView(DestroyAPIView):
    queryset = Subscriptions.objects.all()
    permission_classes = [IsAuthenticated]
