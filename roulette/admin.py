from django.contrib import admin

# Register your models here.
from .models import Agent, Map, Text, AgentSpecificText, MapSpecificText

admin.site.register(Agent)
admin.site.register(Map)
admin.site.register(Text)
admin.site.register(AgentSpecificText)
admin.site.register(MapSpecificText)