import rest_framework.serializers as serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = '__all__'