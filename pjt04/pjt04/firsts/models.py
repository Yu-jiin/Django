from django.db import models

# Create your models here.
class Weather(models.Model):
    date = models.DateField()
    temp_avg_f = models.IntegerField()
    # sqlit3 는 리스트 필드가 없음
    # 문자열로 저장 후, 콤마로 분리 split
    events = models.CharField(max_length=255, blank=True, null=True)
    