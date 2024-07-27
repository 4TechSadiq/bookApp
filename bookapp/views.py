from django.shortcuts import render, redirect

# Create your views here.

from .models import book

def createBook(request):

    Books = book.objects.all() 
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")

        Book=book(title=title,price=price)
        Book.save()

    return render(request,'book.html',{"books":Books})

def listBook(request):
    Books = book.objects.all()
    return render(request,"listbook.html",{"books":Books})


def detailsview(request,book_id):
    Book = book.objects.get(id=book_id)

    return render(request,"detailsview.html",{'book':Book})


def updateBook(request,book_id):
    Book = book.objects.get(id=book_id)

    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")

        Book.title=title
        Book.price = price

        Book.save()
        return redirect("/")


    return render(request,"updateview.html",{"book":Book})
    
def deleteView(request,book_id):
    Book = book.objects.get(id=book_id)

    if request.method=="POST":
        Book.delete()

        return redirect("/")
    return render(request,"delete.html",{'book':Book})