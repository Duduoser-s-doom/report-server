from rest_framework import serializers
from ..models import Report, PDF

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    pdf = PdfSerializer()
    class Meta:
        model = Report
        fields = '__all__'
