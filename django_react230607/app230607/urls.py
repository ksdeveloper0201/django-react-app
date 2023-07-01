from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app230607.views import TaskViewSet, UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)), #上のrouterで定義しているurl情報が入る
    #ManageUserViewはrouterで定義していないためas_viewの形でurlの定義が必要
]

# ModelViewSetを継承している場合（UserViewSet, TaskViewSet）、routerを使う事ができる。
# genericsからとってきたmodeの場合（ManageUserView）は通常のasviewを使った表記を使うことになる。