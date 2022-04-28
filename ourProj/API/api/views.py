from rest_framework.response import Response
from rest_framework.views import APIView
from API.api.serializers import ReportSerializer
from API.models import Report


class ReportView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        for report in request.data.reports:
            newReport = ReportSerializer(data=report)
            if newReport.is_valid():
                newReport.save()
        return Response({"success": True})
    
    def delete(self, request):
        for report in request.data.reports:
            report_model = Report.objects.get(reportId=report.reportId)
            report_serializer = ReportSerializer(report_model)
            report_serializer.delete()
        return Response({"success": True})
   
    def put(self, request):
        for report in request.data.reports:
            report_model = Report.objects.get(reportId=report.reportId)
            report_serializer = ReportSerializer(report_model, data=report)
            if report_serializer.is_valid():
                report_serializer.save()
        return Response({"success": True})