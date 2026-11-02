from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Education, Experience


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Experience
        fields = ['id', 'title', 'description', 'category', 'category_display',
                  'thumbnail', 'started_at', 'ended_at', 'is_ongoing', 'star_count', 'is_starred']
        read_only_fields = ['id', 'is_ongoing']

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot contain only whitespace or HTML tags.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot contain only whitespace or HTML tags.")
        return value

    def validate_thumbnail(self, value):
        if value and not value.lower().startswith(("https://", "http://")):
            raise serializers.ValidationError("Use an HTTP or HTTPS image URL.")
        return value

    def validate(self, attrs):
        start = attrs.get('started_at', getattr(self.instance, 'started_at', None))
        end = attrs.get('ended_at', getattr(self.instance, 'ended_at', None))
        if start and end and end < start:
            raise serializers.ValidationError({'ended_at': 'End date must not precede start date.'})
        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()


class EducationSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    degree_display = serializers.CharField(source="get_degree_display", read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'degree_display', 'field_of_study',
                  'start_year', 'end_year', 'thumbnail', 'description', 'is_current',
                  'star_count', 'is_starred']
        read_only_fields = ['id', 'is_current']

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot contain only whitespace or HTML tags.")
        return value

    def validate_field_of_study(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot contain only whitespace or HTML tags.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot contain only whitespace or HTML tags.")
        return value

    def validate_thumbnail(self, value):
        if value and not value.lower().startswith(("https://", "http://")):
            raise serializers.ValidationError("Use an HTTP or HTTPS image URL.")
        return value

    def validate(self, attrs):
        start = attrs.get('start_year', getattr(self.instance, 'start_year', None))
        end = attrs.get('end_year', getattr(self.instance, 'end_year', None))
        if start is not None and not 1 <= start <= 9999:
            raise serializers.ValidationError({'start_year': 'Use a year between 1 and 9999.'})
        if end is not None and (not 1 <= end <= 9999 or (start and end < start)):
            raise serializers.ValidationError({'end_year': 'End year must be valid and not precede start year.'})
        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()
