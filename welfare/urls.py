from django.urls import path
from .views import *

app_name = "welfare"
urlpatterns = [
    path('choose/', choose, name="choose"),
    path('business/', business, name="business"),
    path('art/', art, name="art"),
    path('social/', social, name="social"),
    path('ai/', ai, name="ai"),
    path('engineering/', engineering, name="engineering"),
    path('buddhism/', buddhism, name="buddhism"),
    path('science/', science, name="science"),
    path('liberal/', liberal, name="liberal"),
    path('police/', police, name="police"),
    path('education/', education, name="education"),
    path('law/', law, name="law"),
    # 카테고리 공간대여
    path('business_room/', business_room, name="business_room"),
    path('art_room/', art_room, name="art_room"),
    path('social_room/', social_room, name="social_room"),
    path('ai_room/', ai_room, name="ai_room"),
    path('engineering_room/', engineering_room, name="engineering_room"),
    path('buddhism_room/', buddhism_room, name="buddhism_room"),
    path('science_room/', science_room, name="science_room"),
    path('liberal_room/', liberal_room, name="liberal_room"),
    path('police_room/', police_room, name="police_room"),
    path('education_room/', education_room, name="education_room"),
    path('law_room/', law_room, name="law_room"),
    # 카테고리 물품대여
    path('business_material/', business_material, name="business_material"),
    path('art_material/', art_material, name="art_material"),
    path('social_material/', social_material, name="social_material"),
    path('ai_material/', ai_material, name="ai_material"),
    path('engineering_material/', engineering_material, name="engineering_material"),
    path('buddhism_material/', buddhism_material, name="buddhism_material"),
    path('science_material/', science_material, name="science_material"),
    path('liberal_material/', liberal_material, name="liberal_material"),
    path('police_material/', police_material, name="police_material"),
    path('education_material/', education_material, name="education_material"),
    path('law_material/', law_material, name="law_material"),
    # 나머지
    path('mainpage/', mainpage, name="mainpage"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('delete/<int:wefare_id>', delete, name="delete"),
    path('<int:welfare_id>', detail, name="detail"),
    path('review/<int:welfare_id>', review, name="review"),
    path('update/<int:welfare_id>', update, name="update"),
    # 댓글
    path('comment_likes/<int:comment_id>', comment_likes, name="comment_likes"),
    path('delete_comment/<int:comment_id>', delete_comment, name="delete_comment"),
    path('edit_comment/<int:comment_id>', edit_comment, name="edit_comment"),
    # 좋아요
    path('welfare_like_toggle', welfare_like_toggle, name="welfare_like_toggle"),
    path('comment_like_toggle', comment_like_toggle, name="comment_like_toggle"),
    path('likes/<int:welfare_id>', detail_likes, name="detail_likes"),
]