# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Transform, Area

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CanalsL(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    rn_i_id = models.CharField(max_length=256, blank=True, null=True)
    rex = models.CharField(max_length=256, blank=True, null=True)
    hyp = models.SmallIntegerField(blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    fun = models.SmallIntegerField(blank=True, null=True)
    nvs = models.SmallIntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tr = models.CharField(max_length=10, blank=True, null=True)
    longpath = models.FloatField(blank=True, null=True)
    cum_len = models.FloatField(blank=True, null=True)
    pente = models.FloatField(blank=True, null=True)
    cgnelin = models.IntegerField(blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    erm_id = models.CharField(max_length=256, blank=True, null=True)
    monot_z = models.SmallIntegerField(blank=True, null=True)
    length_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    tnode = models.CharField(max_length=255, blank=True, null=True)
    strahler = models.FloatField(blank=True, null=True)
    nametxtint = models.CharField(max_length=254, blank=True, null=True)
    nametext = models.CharField(max_length=254, blank=True, null=True)
    nextupid = models.CharField(max_length=255, blank=True, null=True)
    nextdownid = models.CharField(max_length=255, blank=True, null=True)
    fnode = models.CharField(max_length=255, blank=True, null=True)
    catchid = models.IntegerField(blank=True, null=True)
    pfafstetter = models.CharField(max_length=255, blank=True, null=True)
    shape = models.MultiLineStringField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canals_l'


class CanalsP(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canals_p'


class CoastalP(models.Model):
    objectid = models.AutoField(primary_key=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    basindistrict = models.CharField(max_length=50, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coastal_p'


class Culverts(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    elev = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.PointField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'culverts'


class DitchesL(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    rn_i_id = models.CharField(max_length=256, blank=True, null=True)
    rex = models.CharField(max_length=256, blank=True, null=True)
    hyp = models.SmallIntegerField(blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    fun = models.SmallIntegerField(blank=True, null=True)
    nvs = models.SmallIntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tr = models.CharField(max_length=10, blank=True, null=True)
    longpath = models.FloatField(blank=True, null=True)
    cum_len = models.FloatField(blank=True, null=True)
    pente = models.FloatField(blank=True, null=True)
    cgnelin = models.IntegerField(blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    erm_id = models.CharField(max_length=256, blank=True, null=True)
    monot_z = models.SmallIntegerField(blank=True, null=True)
    length_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    tnode = models.CharField(max_length=255, blank=True, null=True)
    strahler = models.FloatField(blank=True, null=True)
    nametxtint = models.CharField(max_length=254, blank=True, null=True)
    nametext = models.CharField(max_length=254, blank=True, null=True)
    nextupid = models.CharField(max_length=255, blank=True, null=True)
    nextdownid = models.CharField(max_length=255, blank=True, null=True)
    fnode = models.CharField(max_length=255, blank=True, null=True)
    catchid = models.IntegerField(blank=True, null=True)
    pfafstetter = models.CharField(max_length=255, blank=True, null=True)
    shape = models.MultiLineStringField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ditches_l'


class DitchesP(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ditches_p'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EuDem(models.Model):
    rid = models.AutoField(primary_key=True)
    rast = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eu_dem'


class Inlandwater(models.Model):
    objectid = models.AutoField(primary_key=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    nam = models.CharField(max_length=256, blank=True, null=True)
    lan = models.CharField(max_length=256, blank=True, null=True)
    rex = models.CharField(max_length=256, blank=True, null=True)
    hyp = models.SmallIntegerField(blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    fun = models.SmallIntegerField(blank=True, null=True)
    nvs = models.SmallIntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    perimeter = models.IntegerField(blank=True, null=True)
    wso_id = models.IntegerField(blank=True, null=True)
    upstr_area = models.FloatField(blank=True, null=True)
    system_cd = models.CharField(max_length=1, blank=True, null=True)
    sea_cd = models.IntegerField(blank=True, null=True)
    lke_type = models.CharField(max_length=1, blank=True, null=True)
    lakid = models.CharField(max_length=10, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    ccm_id = models.IntegerField(blank=True, null=True)
    erm_id = models.CharField(max_length=256, blank=True, null=True)
    window = models.IntegerField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    lakout = models.SmallIntegerField(blank=True, null=True)
    lakin = models.SmallIntegerField(blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inlandwater'


class Nodes(models.Model):
    objectid = models.AutoField(primary_key=True)
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    wmt = models.IntegerField(blank=True, null=True)
    hydronodct = models.CharField(max_length=256, blank=True, null=True)
    len_tom = models.FloatField(blank=True, null=True)
    num_seg = models.SmallIntegerField(blank=True, null=True)
    elev = models.FloatField(blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    nodetype = models.CharField(max_length=256, blank=True, null=True)
    eu_dam_id = models.CharField(max_length=256, blank=True, null=True)
    nat_dam_id = models.CharField(max_length=256, blank=True, null=True)
    dam_mars = models.CharField(max_length=256, blank=True, null=True)
    dam_grand = models.CharField(max_length=256, blank=True, null=True)
    dam_ecrins = models.CharField(max_length=256, blank=True, null=True)
    dam_nam = models.CharField(max_length=256, blank=True, null=True)
    dam_namalt = models.CharField(max_length=256, blank=True, null=True)
    dam_use = models.CharField(max_length=256, blank=True, null=True)
    dam_height = models.FloatField(blank=True, null=True)
    dam_width = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    shape = models.PointField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes'


class PlPlot3857(models.Model):
    fid = models.AutoField(primary_key=True)
    gml_id = models.CharField(blank=True, null=True)
    id_dzialki = models.CharField(max_length=22, blank=True, null=True)
    numer_dzialki = models.CharField(max_length=8, blank=True, null=True)
    numer_obrebu = models.IntegerField(blank=True, null=True)
    numer_jednostki = models.CharField(max_length=8, blank=True, null=True)
    nazwa_obrebu = models.CharField(max_length=24, blank=True, null=True)
    nazwa_gminy = models.CharField(max_length=29, blank=True, null=True)
    data = models.CharField(max_length=26, blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857, blank=True, null=True, spatial_index=True, geography=True)
    area = models.FloatField(db_index=True)
    
    # @classmethod
    # def filter_by_area(cls, area_gte):
    #     # Filter the objects based on the area size
    #     # area_condition = Area(sq_m=10000)
    #     # print(area_condition.sq_m)
        
    #     # print(area_condition)
    #     # filtered_objects = PlPlot3857.objects.annotate(area1=Area(Transform('geom', 3857)))  # 1 hectare = 10000 square meters, so 10 hectares = 100000 square meters
    #     # for obj in filtered_objects:
    #     #     print(obj.area1.sq_m)
    #     #     obj.area = obj.area1.sq_m
    #     #     obj.save()
            
    #     return filtered_objects
    
    class Meta:
        # managed = False
        db_table = 'pl_plot3857'
        # indexes = [
        #     models.Index(fields=['area']),            
        # ]
        # Set indexing on the geom field

        indexes = [
            models.Index(fields=['area']),
            models.Index(fields=['geom'], name='idx_plplot_geom'),
            models.Index(fields=['geom'], name='idx_plplot_geom_spatial'),
        ]
        
    


class PlPlot4326(models.Model):
    fid = models.AutoField(primary_key=True)
    gml_id = models.CharField(blank=True, null=True)
    id_dzialki = models.CharField(max_length=22, blank=True, null=True)
    numer_dzialki = models.CharField(max_length=8, blank=True, null=True)
    numer_obrebu = models.IntegerField(blank=True, null=True)
    numer_jednostki = models.CharField(max_length=8, blank=True, null=True)
    nazwa_obrebu = models.CharField(max_length=24, blank=True, null=True)
    nazwa_gminy = models.CharField(max_length=29, blank=True, null=True)
    data = models.CharField(max_length=26, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_plot4326'


class PlRiver3857(models.Model):
    fid = models.AutoField(primary_key=True)
    rzeki_r_field = models.FloatField(db_column='rzeki_r_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rzeki_r_id = models.FloatField(blank=True, null=True)
    id_hyd_r = models.FloatField(blank=True, null=True)
    rzad = models.IntegerField(blank=True, null=True)
    dlug = models.FloatField(blank=True, null=True)
    id_hyd_rc = models.FloatField(blank=True, null=True)
    naz_rzeki = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiLineStringField(srid=3857, blank=True, null=True, spatial_index = True, geography=True)
    r_width = models.FloatField(db_index=True)
    # objects = models.GeoManager()
    class Meta:
        managed = False
        db_table = 'pl_river3857'
                
        indexes = [
            models.Index(fields=['dlug']),
            models.Index(fields=['r_width']),
            models.Index(fields=['dlug','r_width']),
            models.Index(fields=['geom'], name='idx_plriver_geom'),
            models.Index(fields=['geom'], name='idx_plriver_geom_spatial'),
        ]
    


class PlRiver4326(models.Model):
    fid = models.AutoField(primary_key=True)
    rzeki_r_field = models.FloatField(db_column='rzeki_r_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rzeki_r_id = models.FloatField(blank=True, null=True)
    id_hyd_r = models.FloatField(blank=True, null=True)
    rzad = models.IntegerField(blank=True, null=True)
    dlug = models.FloatField(blank=True, null=True)
    id_hyd_rc = models.FloatField(blank=True, null=True)
    naz_rzeki = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_river4326'


class PlRiver92(models.Model):
    fid = models.AutoField(primary_key=True)
    rzeki_r_field = models.FloatField(db_column='rzeki_r_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rzeki_r_id = models.FloatField(blank=True, null=True)
    id_hyd_r = models.FloatField(blank=True, null=True)
    rzad = models.IntegerField(blank=True, null=True)
    dlug = models.FloatField(blank=True, null=True)
    id_hyd_rc = models.FloatField(blank=True, null=True)
    naz_rzeki = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiLineStringField(srid=900915, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_river92'


class PlanetOsmLine(models.Model):
    osm_id = models.BigIntegerField()
    access = models.TextField(blank=True, null=True)
    iso3166_1 = models.TextField(db_column='ISO3166-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    addr_country = models.TextField(db_column='addr:country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.MultiLineStringField()

    class Meta:
        managed = False
        db_table = 'planet_osm_line'


class PlanetOsmPoint(models.Model):
    osm_id = models.BigIntegerField()
    access = models.TextField(blank=True, null=True)
    iso3166_1 = models.TextField(db_column='ISO3166-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    addr_country = models.TextField(db_column='addr:country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    capital = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    ele = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way = models.PointField()

    class Meta:
        managed = False
        db_table = 'planet_osm_point'


class PlanetOsmPolygon(models.Model):
    osm_id = models.BigIntegerField()
    access = models.TextField(blank=True, null=True)
    iso3166_1 = models.TextField(db_column='ISO3166-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    addr_country = models.TextField(db_column='addr:country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'planet_osm_polygon'


class PlanetOsmRoads(models.Model):
    osm_id = models.BigIntegerField()
    access = models.TextField(blank=True, null=True)
    iso3166_1 = models.TextField(db_column='ISO3166-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    addr_country = models.TextField(db_column='addr:country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.MultiLineStringField()

    class Meta:
        managed = False
        db_table = 'planet_osm_roads'


class RiverNetL(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    rn_i_id = models.CharField(max_length=256, blank=True, null=True)
    rex = models.CharField(max_length=256, blank=True, null=True)
    hyp = models.SmallIntegerField(blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    fun = models.SmallIntegerField(blank=True, null=True)
    nvs = models.SmallIntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tr = models.CharField(max_length=10, blank=True, null=True)
    longpath = models.FloatField(blank=True, null=True)
    cum_len = models.FloatField(blank=True, null=True)
    pente = models.FloatField(blank=True, null=True)
    cgnelin = models.IntegerField(blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    erm_id = models.CharField(max_length=256, blank=True, null=True)
    mc = models.SmallIntegerField(blank=True, null=True)
    monot_z = models.SmallIntegerField(blank=True, null=True)
    length_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    tnode = models.CharField(max_length=255, blank=True, null=True)
    strahler = models.FloatField(blank=True, null=True)
    nametxtint = models.CharField(max_length=254, blank=True, null=True)
    nametext = models.CharField(max_length=254, blank=True, null=True)
    nextupid = models.CharField(max_length=255, blank=True, null=True)
    nextdownid = models.CharField(max_length=255, blank=True, null=True)
    fnode = models.CharField(max_length=255, blank=True, null=True)
    catchid = models.IntegerField(blank=True, null=True)
    pfafstetter = models.CharField(max_length=255, blank=True, null=True)
    shape = models.MultiLineStringField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'river_net_l'


class RiverNetP(models.Model):
    objectid = models.AutoField(primary_key=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'river_net_p'


class Riverbasins(models.Model):
    objectid = models.AutoField(primary_key=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riverbasins'


class TransitP(models.Model):
    objectid = models.AutoField(primary_key=True)
    thematicid = models.CharField(max_length=42, blank=True, null=True)
    dfdd = models.CharField(max_length=5, blank=True, null=True)
    beglifever = models.DateTimeField(blank=True, null=True)
    endlifever = models.DateTimeField(blank=True, null=True)
    updat_by = models.CharField(max_length=15, blank=True, null=True)
    updat_when = models.DateTimeField(blank=True, null=True)
    elev = models.FloatField(blank=True, null=True)
    object_id = models.CharField(max_length=256, blank=True, null=True)
    area_geo = models.FloatField(blank=True, null=True)
    inspire_id = models.CharField(max_length=256, blank=True, null=True)
    shape = models.MultiPolygonField(srid=900914, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transit_p'
