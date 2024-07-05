from django.db import models

#models 모듈에서 Model 상속
class HelloWorld(models.Model):
    text = models.CharField(max_length=255,null=False)