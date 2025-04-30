from datetime import timezone
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,exceptions
from api.serializers import ContactSerializer, GroupSerializer, NewsletterSerializer, PostPublishSerializer, UserSerializer,PostSerializer,TagSerializer,CategorySerializer
from newspaper.models import Category, Contact, NewsLetter,Tag,Post
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    

class CategoryViewSet(viewsets.ModelViewSet):
   
    queryset = Category.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()

class TagViewSet(viewsets.ModelViewSet):
    
    queryset = Tag.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ["list","retrive"]:
            queryset= queryset.filter(status="active",published_at__isnull=False)

            from django.db.models import Q
            search_term = self.request.query_params.get("search",None)
            if search_term:
                queryset= queryset.filter(
                    Q(title__icontains=search_term) | Q(content__icontains=search_term))
                
        return queryset

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count +=1
        instance.save(update_fields=["views_count"])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
    
class PostListByCategoryView(ListAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            status = "active",
            published_at__isnull = False,
            category = self.kwargs["category_id"],
        )

        return queryset
    
class DraftListView(ListAPIView):
    queryset=Post.objects.filter(published_at__isnull=True)
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

class DraftDetailView(RetrieveAPIView):
    queryset=Post.objects.filter(published_at__isnull=True)
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

class NewsletterViewSet(viewsets.ModelViewSet):
    
    queryset = NewsLetter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve","destroy"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(request.method)
    
class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve","destroy"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(request.method)

def PostPublishViewSet(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def Post(self,request,*args,**kwargs):
        serializer = PostPublishSerializer(data=request.data)
        if serializer.is_valid(raise_expection=True):
            data = serializer.data

            post= Post.objects.get(pk=data["id"])
            post.published_at = timezone.now()
            post.save()

            serializer_data = PostSerializer(post).data
            return Response(serializer_data,status=status.HTTP_200_ok)