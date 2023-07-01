from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # ↓レスポンスの際に表示する値
        fields = ('id', 'username', 'password')
        extra_kwarts = {'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        # ↓この処理を行うことでハッシュ化した値をDBに保存することができる。
        user = User.objects.create_user(**validated_data)
        # ↓userを新規で作成した際に、同時にトークンを生成してDBに登録する。
        Token.objects.create(user=user)
        return user
    
class TaskSerializer(serializers.ModelSerializer):

    # read_only=Trueとすることでgetメソッドでアクセスした場合、下の二つを種痘することができるが、postメソッドの場合は不要となる。
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at']