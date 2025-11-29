from rest_framework import serializers
from .models import (UserProfile, Category, SubCategory,
                     Level, Course, Lesson, AssignMent,
                     Exam, Questions, Option, Certificate,
                     Review)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_image', 'first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CourseListSerializer(serializers.ModelSerializer):
    subcategory = SubCategoryListSerializer()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'created_by',
                  'price', 'subcategory']


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['level']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']


class AssignMentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignMent
        fields = ['title', 'description', 'duo_date']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    subcategory = SubCategoryListSerializer()
    lessons = LessonSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    level = LevelSerializer(many=True)
    assignments = AssignMentSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'lessons', 'created_by',
                  'created_at', 'updated_at', 'price', 'level',
                  'assignments', 'description', 'reviews',
                  'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_avg_rating()


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    courses = CourseDetailSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'courses']


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question_name']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option_name', 'option_type']


class ExamSerializer(serializers.ModelSerializer):
    quests = QuestionsSerializer(many=True, read_only=True)
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['title', 'duration', 'quests', 'options']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'