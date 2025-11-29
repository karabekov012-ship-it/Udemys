from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CategoryListAPIView, CategoryDetailAPIView,
                    SubCategoryListAPIView, SubCategoryDetailAPIView,
                    CourseListAPIView, CourseDetailAPIView,
                    ReviewCreateAPIView, ReviewEditAPIView,
                    CertificateViewSet, CreateCourseViewSet,
                    RegisterView, CustomLoginView, LogoutView)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'certifications', CertificateViewSet)
router.register(r'course_create', CreateCourseViewSet)

urlpatterns = [
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('subcategories/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('courses/', CourseListAPIView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
]