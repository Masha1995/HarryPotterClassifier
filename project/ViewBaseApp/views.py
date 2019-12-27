from django.shortcuts import render
from DatabaseManagerApp.models import Article, TextClass

def allClasses(request):
    classes = TextClass.objects.all().order_by("description")
    quantity = Article.objects.all().count()
    return render(request, "ViewBase/allclasses.html",\
                  context={"classes": classes, "quantity": quantity})

def classArticles(request, class_name):
    # проверка на наличие класса в базе
    # если запрашиваемый класс не существует, сообщаем, что такого класса нет
    try:
        currentTextClass = TextClass.objects.get(name = class_name)
    except Exception:
        return render(request, "pagenotfound.html")
    
    articles = Article.objects.filter(textclassid = currentTextClass.id).order_by("title")
    quantity = Article.objects.filter(textclassid = currentTextClass.id).count()
    return render(request, "ViewBase/classarticles.html",\
                  context={"class": currentTextClass, "articles": articles, "quantity": quantity})

def article(request, article_id):
    # получение статьи из базы по id
    # если статьи с таким id не существует, сообщаем, что такой статьи нет
    try:
        currentArticle = Article.objects.get(id = article_id)
    except Exception:
        return render(request, "pagenotfound.html")
    
    currentTextClass = TextClass.objects.get(id = currentArticle.textclassid)
    return render(request, "ViewBase/article.html",\
                  context={"article": currentArticle, "class": currentTextClass})
