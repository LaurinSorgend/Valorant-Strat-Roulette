from django.db import models
from django.contrib import admin

# Create your models here.
class Text(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    random_player = models.BooleanField(default=False)
    attacking = models.BooleanField(default=False)
    defending = models.BooleanField(default=False)

    def __str__(self):
        if len(self.text) > 48:
            return self.text[:48]
        return self.text


class Agent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_en = models.CharField(max_length=30)
    @admin.display(empty_value="???")
    def __str__(self):
        return self.name_en


class Map(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_en = models.CharField(max_length=30)

    def __str__(self):
        return self.name_en


class AgentSpecificText(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    text = models.TextField()
    random_player = models.BooleanField(default=False)
    attacking = models.BooleanField(default=False)
    defending = models.BooleanField(default=False)

    def __str__(self):
        if len(self.text) > 48:
            return self.agent.name_en + ": " + self.text[:48]
        return self.agent.name_en + ": " + self.text


class MapSpecificText(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    text = models.TextField()
    random_player = models.BooleanField(default=False)
    attacking = models.BooleanField(default=False)
    defending = models.BooleanField(default=False)

    def __str__(self):
        if len(self.text) > 48:
            return self.map.name_en + ": " + self.text[:48]
        return self.map.name_en + ": " + self.text
