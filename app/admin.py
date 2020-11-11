from django.contrib import admin
from django.contrib import admin
# Register your models here.
from app import models
admin.site.register(models.User)
admin.site.register(models.Team)
admin.site.register(models.agri_img)
admin.site.register(models.serviceobject_img)
admin.site.register(models.consultant_content_img)
admin.site.register(models.training_courses_img)
admin.site.register(models.index_img)
admin.site.register(models.database_img)
admin.site.register(models.simulation_platform_img)
admin.site.register(models.solution_img)
admin.site.register(models.produce_img)
