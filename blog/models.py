from django.db import models
from django.utils import timezone
#from import는 다른 파일에 있는것 추가
# Create your models here.

class Post(models.Model):
	#model = object, model 정의
	# class 는 특별한 키워드로, 객체를 정의
	# Post 는 모델의 이름 
	# models 은 Post가 장고 모델임을 의미. 이 코드 때문에
	# 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됨 

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #짧은 문자열
    text = models.TextField() #글자 수 제한 없음
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
