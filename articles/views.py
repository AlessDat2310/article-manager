from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404, redirect

import json
from django.shortcuts import get_object_or_404

class ArticleDetailView(View):

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        return render(request, "articles/detail.html", {"article": article})
    
class ArticleUpdateView(View):

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(instance=article)
        return render(request, "articles/edit.html", {"form": form, "article": article})

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('article-detail', pk=article.pk)

        return render(request, "articles/edit.html", {"form": form, "article": article})
    
class ArticleDeleteView(View):

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('article-list')
    
class ArticleCreateView(View):

    def get(self, request):
        form = ArticleForm()
        return render(request, "articles/new_article_form.html", {"form": form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
        return render(request, "articles/new_article_form.html", {"form": form})
    

class ArticleListView(View):

    def get(self, request):
        articles = Article.objects.all()
        return render(request, "articles/list.html", {"articles": articles})
    



    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        name = data.get("name")
        content = data.get("content")

        if not name:
            return JsonResponse({"error": "El campo 'name' es obligatorio"}, status=400)

        article = Article.objects.create(name=name, content=content)

        return JsonResponse(
            {"ID DEL ARTICULO": article.id, "NOMBRE": article.name, "DESCRIPCIÓN": article.content},
            status=201
        )

    def delete(self, request):
        Article.objects.all().delete()
        return JsonResponse({"deleted": True})
    
