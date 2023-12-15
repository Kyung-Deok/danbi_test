from django.db import models

class TimeStampModel(models.Model):
    ''' 재사용 하는 모델 '''
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성_타임스탬프')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정_타임스탬프')

    class Meta:
        abstract = True