from django.db import models


# Create your models here.
class Text(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()

    def __str__(self):
        if len(self.text) > 16:
            return self.text[:16]
        return self.text


class Agent(models.Model):
    name_en = models.CharField(max_length=30)

    def __str__(self):
        return self.name_en

class Map(models.Model):
    name_en = models.CharField(max_length=30)

    def __str__(self):
        return self.name_en

class AgentSpecificText(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        if len(self.text) > 16:
            return self.text[:16]
        return self.text

class MapSpecificText(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        if len(self.text) > 16:
            return self.text[:16]
        return self.text