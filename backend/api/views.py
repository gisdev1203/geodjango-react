from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import PlRiver3857, PlPlot3857
# from .serializers import *
from django.core.serializers import serialize
from django.contrib.gis.measure import D


from django.contrib.gis.db.models.functions import Transform, Area, Distance
import json
import random

# Create your views here.

# def front(request):
#     context = { }
#     return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def complex_Search(request):
    print(request.method)
    if request.method == 'GET':
        print(request.data)
        
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':

        river_data = request.data.get('river')
        r_length = river_data.get('R_Length')
        r_width = river_data.get('R_Width')
        filter_condition = {'dlug__gte': float(r_length),
                            'r_width__gte': float(r_width)
                            }
        riverfilter = PlRiver3857.objects.filter(**filter_condition)
        print(f"river_count: {riverfilter.count()}")
        geoData = serialize("geojson", riverfilter, geometry_field="geom", fields=["naz_rzeki"])
        
        # river_queryset = PlRiver3857.objects.select_related('') #annotate(distance=Distance('geom', models.F('plot__geom'))).filter(distance__lte=1000)
        # condition = {'area__lte': float(5000)}
        # plotfilter = PlPlot3857.objects.filter(**condition)
        # print(f"plot_count: {plotfilter.count()}")
        
        # plot_temp = PlPlot3857.objects.filter(geom__area_lte=500)
        
        #create a buffer around the polyline object
        # buffer_polyline =
        # for riverline in riverfilter:
        #     #create a buffer around the riverline object
        #     buffer_polyline = riverline.geom.buffer(1000)
        #     print(buffer_polyline)
            # contain_plot = plotfilter.filter(geom__intersects=buffer_polyline )
            # if contain_plot.count() > 0:
            #     print('--------------------------')
            #     print(contain_plot)
            #     print('**************************************')
        
        # # print(f"plot_temp {plot_temp.count()}")
        # for plot in plotfilter:
        #     # print(plot.geom.centroid)
        #     point = plot.geom.centroid
        #     data = riverfilter.filter(geom__distance_lte=(point, D(km=0.001)))
        #     if data.count() > 0:
        #         print("--------------------")
        #         print(data)
        #         print("-------------------")
        
        # plotfilter.prefetch_related(riverfilter)
        
        # geojson = serializers('geojson', queryset, geometry_field='geom')
        
        # print(geojson)
        
        return Response(geoData)
        
        
        