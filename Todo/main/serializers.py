from rest_framework import serializers
from .models import TaskModel

import jdatetime


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()
    
    class Meta:
        model = TaskModel
        exclude = ['created_at', 'updated_at']
        
    def get_created(self, obj):
        jalali_datetime = jdatetime.datetime.fromgregorian(
            datetime=obj.created_at
        )
        return jalali_datetime.strftime('%Y/%m/%d - %H:%M')
    
    def get_updated(self, obj):
        jalali_datetime = jdatetime.datetime.fromgregorian(
            datetime=obj.updated_at
        )
        return jalali_datetime.strftime('%Y/%m/%d - %H:%M')