from django.shortcuts import get_object_or_404, render, redirect
from yoolink.ycms.models import FAQ, Message, Product, TextContent, fileentry, Galerie, GaleryImage
import datetime
from django.http import HttpResponseRedirect


def load_index(request):
    faq = FAQ.objects.all()

    context = {
        'FAQ': faq,
    }

    # Text Contents
    if TextContent.objects.filter(name="main_hero").exists():
        context["heroText"] = TextContent.objects.get(name='main_hero')

    if TextContent.objects.filter(name="main_responsive").exists():
        context["responsiveText"] = TextContent.objects.get(name='main_responsive')

    if TextContent.objects.filter(name="main_cms").exists():
        context["cmsText"] = TextContent.objects.get(name='main_cms')

    if TextContent.objects.filter(name="main_price").exists():
        context["priceText"] = TextContent.objects.get(name='main_price')

    if TextContent.objects.filter(name="main_team").exists():
        context["teamText"] = TextContent.objects.get(name='main_team')

    # Galery
    if Galerie.objects.filter(place='main_hero').exists():
        context["heroImages"] = Galerie.objects.get(place='main_hero').images.all()
        
    if Galerie.objects.filter(place='main_responsive_desktop').exists():
        context['responsiveDesktopImages'] = Galerie.objects.get(place='main_responsive_desktop').images.all()
        
    if Galerie.objects.filter(place='main_responsive_handy').exists():
        context['responsiveHandyImages'] = Galerie.objects.get(place='main_responsive_handy').images.all()

    # Images
    if fileentry.objects.filter(place='main_cms').exists():
        context["cmsImage"] = fileentry.objects.get(place='main_cms')

    return render(request, 'pages/index.html', context=context)

def shop(request):
   return render(request, 'pages/shop.html', context={"products": Product.objects.filter(is_active=True)})

def detail(request, product_id):
     product = get_object_or_404(Product, id=product_id)
     return render(request, 'pages/detail.html', context={"product": product})
