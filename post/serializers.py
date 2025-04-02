from rest_framework import serializers
from core import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id' ,'name','description']
        read_only_fields = ['id']

class PostSerializer(serializers.ModelSerializer):
    Category = CategorySerializer(many = True , required = False)
    def _get_or_create_category(self , categories , post):
        auth_user = self.context['request'].user
        for category in categories:
            category_obj , created = models.Category.objects.get_or_create(
                **category,
            )
            post.Category.add(category_obj)
    class Meta:
        model = models.Post
        fields =['id' , 'title','content' , 'created_at' , 'author' , 'status','Category' ,'user' ]

        extra_kwargs = {
            'user':{
                'read_only':True
            }
        }



    def create(self, validated_data):
        category = validated_data.pop('Category', [])
        post = models.Post.objects.create(**validated_data)
        # post.Category.add(category)
        self._get_or_create_category(category  , post)

        return post

    # def update(self, instance, validated_data):
    #     # category = validated_data.pop('Category' , [])
    #     # self._get_or_create_category(category , instance)
    #     instance.save()
    #     return instance



