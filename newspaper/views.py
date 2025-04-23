from datetime import timedelta
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,DetailView, View
from newspaper.forms import CommentForm, ContactForm
from newspaper.models import Category, Contact, Post, Advertisement, Tag , Newsletter
from django.contrib.messages.views import SuccessMessageMixin


class SidebarMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["popular_posts"]=Post.objects.filter(published_at__isnull=False,status="active").order_by("-published_at")[:5]

        context["advertisement"] =Advertisement.objects.all().order_by("-created_at").first()

        return context


class HomeView(SidebarMixin, ListView):
    model = Post
    template_name = "newsportal/home.html"
    context_object_name = "posts"

    queryset = Post.objects.filter(
        published_at__isnull=False, status = "active"
    ).order_by("-published_at")[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False,status="active")
            .order_by("-published_at","views_count")
            .first()
        )

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(published_at__isnull=False,status="active", published_at__gte=one_week_ago).order_by("-published_at", "-views_count")[:5]

        return context
    

class PostListView(SidebarMixin, ListView):
    model = Post
    template_name = "newsportal/list/list.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull = False, status = "active").order_by("-published_at")


class PostByCategoryView(SidebarMixin,ListView):
    model=Post
    template_name="newsportal/list/list.html"
    context_object_name="posts"
    paginate_by=1

    def get_queryset(self):
        query= super().get_queryset()
        query =query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["category_id"],
        ).order_by("-published_at")

        return query


class TagListView(ListView):
    model = Tag
    template_name = "newsportal/tags.html"
    context_object_name = "tags"


class CategoryListView(ListView):
    model = Category
    template_name = "newsportal/categories.html"
    context_object_name = "categories"


class AboutUsView(ListView):
    model = Post
    template_name = "newsportal/about_us.html"


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = "newsportal/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    success_message = "Your message have been sent sucessfully!"


class PostDetailView(SidebarMixin, DetailView):
    model = Post
    template_name = "newsportal/detail/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False, status="active")
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_posts"] = Post.objects.filter(published_at__isnull=False, status="active", category=self.object.category).order_by("-published_at","-views_count") [:2] 
        return context
    
class TagDetailView(SidebarMixin, DetailView):
    model = Tag
    template_name = "newsportal/tag_detail.html" 
    context_object_name = "tag"

class CommentView(View):
    def post(self, request, *args, **kwargs):
        post_id = request.POST["post"]
        user_id = request.user.id

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("post-detail",post_id)
        
        else:
            post = Post.objects.get(pk=post_id)
            popular_posts =Post.objects.filter(published_at__isnull=False,status="active").order_by("-published_at")[:5]

            advertisement =Advertisement.objects.all().order_by("-created_at").first()
            return render(
                request,
                "newsportal/detail/detail.html",
                {
                    "post":post,
                  "form":form,
                  "popular_posts":popular_posts,
                  "advertisement":advertisement,
                  },
            )
        



   