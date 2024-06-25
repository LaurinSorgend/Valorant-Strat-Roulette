from django.contrib import admin

# Register your models here.
from .models import Agent, Map, Text, AgentSpecificText, MapSpecificText


# admin.site.register(Map)
admin.site.register(Text)
admin.site.register(AgentSpecificText)
admin.site.register(MapSpecificText)


class AgentSpecificTextInLine(admin.TabularInline):
    model = AgentSpecificText
    extra = 1


class AgentAdmin(admin.ModelAdmin):
    inlines = [AgentSpecificTextInLine]


class MapSpecificTextInLine(admin.TabularInline):
    model = MapSpecificText
    extra = 1


class MapAdmin(admin.ModelAdmin):
    inlines = [MapSpecificTextInLine]


admin.site.register(Map, MapAdmin)


admin.site.register(Agent, AgentAdmin)
