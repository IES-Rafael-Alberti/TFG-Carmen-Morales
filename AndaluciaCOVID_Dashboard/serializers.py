from rest_framework import serializers

from .models import *

class ProvinceSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='ccaa.name')
    class Meta:
        model = Province
        fields = ('id', 'name', 'region_name','poblation','confirmedPDIA','totalConfirmed','tasa14days','tasa7days','deceased','recovered')      


class TownshipSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='distrit.name')
    class Meta:
        model = Township
        fields = ('id', 'name', 'district_name','poblation','confirmedPDIA','totalConfirmed','tasa14days','tasa7days','deceased','recovered')      

class DistrictSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(source = 'province.name')
    class Meta:
        model = District
        fields = ('id', 'name', 'province_name')      

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'poblation','confirmedPDIA','totalConfirmed','tasa14days','tasa7days','deceased','recovered')                

class TownshipHistoricDetailSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='distr.name')
    class Meta:
        model = HistoricTownship
        fields = ('id', 'date', 'district_name', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')           

class RegionHistoricDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricGeneral
        fields = ('id', 'date', 'cAutonoma', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')          

class ProvinceHistoricDetailSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(source='province.name')
    class Meta:
        model = HistoricProvince
        fields = ('id', 'date', 'province_name', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')          

class RegionAccumulatedSerializer(serializers.ModelSerializer):
    ccaa_name = serializers.CharField(source = 'ccaa.name')
    class Meta:
        model = AcumulatedRegion
        fields = ('id', 'date', 'ccaa_name', 'confirmedPDIA', 'aument', 'pcr14days','pcr7days','totalConfirmed','Hospitalized','ICU','deceased','recovered')

class ProvinceAccumulatedSerializer(serializers.ModelSerializer):
    ccaa_name = serializers.CharField(source = 'ccaa.name')
    class Meta:
        model = AcumulatedProvinces
        fields = ('id', 'date', 'ccaa_name', 'confirmedPDIA', 'aument', 'pcr14days','pcr7days','totalConfirmed','Hospitalized','ICU','deceased','recovered')          