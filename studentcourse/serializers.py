from rest_framework.serializers import ModelSerializer
from .models import Student,ElectiveCourse


class BaseSerializer(ModelSerializer):
    class Meta:
        fields = ["created_at","updated_at"]
        fields_read_only = ["created_at","updated_at"]

class ElectiveCourseSerializer(BaseSerializer):
    class Meta:
        model = ElectiveCourse
        fields = BaseSerializer.Meta.fields + ["course_id","name","duration_in_months","active"]
        
class StudentSerializer(BaseSerializer):
    class Meta:
        model = Student
        fields = BaseSerializer.Meta.fields + ["id_no","name","courses","active"]

    