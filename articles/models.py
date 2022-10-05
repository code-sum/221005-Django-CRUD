from django.db import models

# Create your models here.

'''
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간 / 글 수정시간(자동으로 기록, 날짜/시간)
'''

# 1. 모델 설계 (=DB 스키마 설계)
# Article 은 models 에 있는 Model 을 상속 받음
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 2. 설계한 모델을 DB에 반영