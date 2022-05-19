from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from ..models import Report, PDF

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'

class ReportSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    pdf = PdfSerializer()
    class Meta:
        model = Report
        fields = '__all__'
    def create(self, validated_data):
        pdf_data = validated_data.pop('pdf')
        pdf = PDF.objects.create(**pdf_data)
        report = Report.objects.create(pdf=pdf, **validated_data)
        return report
