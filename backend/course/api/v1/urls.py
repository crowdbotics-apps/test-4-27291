from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("recording", RecordingViewSet)
router.register("module", ModuleViewSet)
router.register("category", CategoryViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("group", GroupViewSet)
router.register("course", CourseViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("lesson", LessonViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("event", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
