from email import message
from multiprocessing import context
from unicodedata import category
from venv import create
from django.shortcuts import render,redirect
from .models import Category,photo
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.
def about(request):
    return render(request,'photos/about.html')
#Gallery show
def gallery(request):
    categories=Category.objects.all()
    photos=photo.objects.all()
    paginator=Paginator(photos,9)
    page=request.GET.get('page')
    try:
        photos=paginator.page(page)
    except PageNotAnInteger:
        photos=paginator.page(1)
    except EmptyPage:
        photos=paginator.page(paginator.num_pages)
    context={'categories':categories,'photos':photos,'page':page}
    return render(request,'photos/gallery.html',context)

#view photos
#def viewphotos(request):


def viewphotos(request, pk):
    photos = photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photos': photos})

#add photos
def addphotos(request):
#
    categories = Category.objects.all()

    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')

        #if data['category'] !='none':
            #category = Category.objects.get(id=data['category'])
        if data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category=None
        Photos = photo.objects.create(
            category=category,
            description=data['description'],
            image=image,

        )
        return  redirect('gallery')


    context = {'categories': categories}
    return render(request,'photos/add.html',context)


#    path('photo/', views.viewphotos, name='photo'),
