
from rest_framework import viewsets
from posts.models import Post, Tag, Author
from posts.serializers import TagSerializer, AuthorSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
      queryset = Tag.objects.all()
      serializer_class = TagSerializer   


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 



# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics

# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class TagView(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

# class TagDetailView(generics.RetrieveDestroyAPIView):
#       queryset = Tag.objects.all()
#       serializer_class = TagSerializer  



# class AuthorView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorDetailView(generics.RetrieveDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer 







# Create your views here.
# class PostView(APIView):

#     def get(self, request):

#         posts = Post.objects.all()

#         serializer = PostSerializer(posts, many = True)

#         return Response(serializer.data)
    
#     def post(self, request):
        
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
# class PostDetailView(APIView):
#     def get(self, request, id):
#         post= get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post) 
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id) 
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, id=id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id)

#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class TagView(APIView):

#     def get(self, request):

#         tags = Tag.objects.all()

#         serializers = TagSerializer(tags, many=True)

#         return Response(serializers.data)
        
#     def post(self, request):

#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class AuthorView(APIView):

#     def get(self, request):

#         authors = Author.objects.all()

#         serializer = AuthorSerializer(authors, many=True)

#         return Response(serializer.data)
    
#     def post(self, request):

#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




