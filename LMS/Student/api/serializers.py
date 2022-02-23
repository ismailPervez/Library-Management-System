from Student.models import Student
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from Library.models import WishList

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email']

class WishlistSerializer(ModelSerializer):
    book = SerializerMethodField()
    class Meta:
        model = WishList
        fields = ['book', 'student']

    def get_book(self, obj):
        return {'title': obj.book.title, 'pk': obj.book.pk}