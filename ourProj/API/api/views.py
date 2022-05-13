from rest_framework.response import Response
from rest_framework.views import APIView
from API.api.serializers import ReportSerializer
from API.models import Report


class ReportView(APIView):
    def get(self, request):
        q = request.query_params
        page, count, name, group = int(q.get('page')), int(q.get('count')), q.get('name'), q.get('group')
        if name == None and group == None:
            reports = Report.objects.all()
            serializer = ReportSerializer(reports, many=True)
            count_reports = Report.objects.all().count()
            print(reports, count_reports)
            return Response(serializer.data)
        reports = Report.objects.filter(name = name, group = group)[(page-1)*count:page*count]
        serializer = ReportSerializer(reports, many=True)
        count_reports = Report.objects.filter(name = name, group = group).count()
        print(page, count, name, group, count_reports)        
        return Response(serializer.data)

    def post(self, request):
        for report in request.data.get('reports'):
            newReport = ReportSerializer(data=report)
            print(newReport)
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