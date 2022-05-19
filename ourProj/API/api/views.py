from rest_framework.response import Response
from rest_framework.views import APIView
from API.api.serializers import ReportSerializer
from API.models import Report


class ReportView(APIView):
    def get(self, request):
        q = request.query_params
        page, count, name, group = int(q.get('page')), int(q.get('count')), q.get('name'), q.get('group')
        if name == None and group == None:
            reports = Report.objects.all()[(page-1)*count:page*count]
            serializer = ReportSerializer(reports, many=True)
            count_reports = Report.objects.all().count()
            return Response({"reports":serializer.data,"count": count_reports})
        if group == None: group = ""
        if name == None: name = ""
        reports = Report.objects.filter(name__icontains = name, group__icontains = group)[(page-1)*count:page*count]
        serializer = ReportSerializer(reports, many=True)
        count_reports = Report.objects.filter(name__icontains = name, group__icontains = group).count()
        print(page, count, name, group, count_reports)        
        return Response({"reports":serializer.data,"count": count_reports})

    def post(self, request):
        newReports = ReportSerializer(data=request.data.get("reports"), many=True)
        if(newReports.is_valid()):
            newReports.save()
            return Response({"success": True})
        return Response({"success":False})
    
    def delete(self, request):
        for report in request.data.get("reports"):
            report_model = Report.objects.get(reportId=report.get("reportId"))
            report_serializer = ReportSerializer(report_model)
            report_serializer.delete()
        return Response({"success": True})
   
    def put(self, request):
        for report in request.data.get("reports"):
            report_model = Report.objects.get(reportId=report.get("reportId"))
            report_serializer = ReportSerializer(report_model, data=report)
            if report_serializer.is_valid():
                report_serializer.save()
        return Response({"success": True})
        