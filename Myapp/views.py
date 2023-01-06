import csv
from datetime import timedelta, datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht
import xlwt


def home(request):
    return render(request, 'acc.html')

def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'app.html', s)
def table(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'table.html', s)


def chart(request):
    ab = len(Dht.objects.all())
    tab = Dht.objects.all()[ab-72:ab]
    temperature = Dht.objects.latest('dt')
    s = {'tab': tab,'temp': temperature.temp,'dt': temperature.dt}
    return render(request, 'chart.html', s)


def archive(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'archive.html', s)


def history24(request):
    ab=len(Dht.objects.all())
    tab = Dht.objects.all()[ab-72:ab]
    s = {'tab': tab}
    return render(request, 'history24.html', s)


def graph_24h(request):
    ab = len(Dht.objects.all())
    tab = Dht.objects.all()[ab-72:ab]
    s = {'tab': tab}
    return render(request, 'app.html', s)
##xlx
def export_xls24h(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dht24h.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    ab = len(Dht.objects.all())
    queryset = Dht.objects.all()[ab-72:ab]
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def export_xls48h(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dht28h.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    ab = len(Dht.objects.all())
    queryset = Dht.objects.all()[ab - 144:ab]
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def export_xlsweek(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dhtweek.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    queryset = Dht.objects.all()
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
