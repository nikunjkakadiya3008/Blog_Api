from rest_framework import serializers
from core import models
from datetime import datetime
from django.utils.translation import gettext as _


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id' ,'name','description']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id','content','created_at','post','author']
        read_only_fields = ['id' , 'created_at' ]
        extra_kwargs = {
            'author':{
                'read_only':True
            }
        }

    def create(self, validated_data):
        comment = models.Comment.objects.create(**validated_data)
        return comment

class PostSerializer(serializers.ModelSerializer):
    Category= serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all(), many=True, required=False)
    class Meta:
        model = models.Post
        fields =['id' , 'title','content','updated_at' , 'created_at' , 'author' , 'status','Category' ,'user' ]

        extra_kwargs = {
            'user':{
                'read_only':True
            },
            'updated_at':{
                'read_only':True
            }
        }



    def create(self, validated_data):
        categories = validated_data.pop('Category', [])
        for category in categories:
            exist = models.Category.objects.filter(pk =category).exists()
            print(exist)
            if not exist:
                msg =_("Provided Category is not Valid")
                raise serializers.ValidationError(msg)
        post = models.Post.objects.create(**validated_data)
        post.created_at = datetime.now()
        post.Category.set(category)
        # self._get_or_create_category(category  , post)

        return post

    def update(self, instance, validated_data):
        category = validated_data.pop('Category' , [])
        if category:
            instance.Category.clear()
            instance.Category.set(category)
        for attr , value in validated_data.items():
            setattr(instance , attr , value)
        instance.updated_at = datetime.now()
        instance.save()
        return instance




