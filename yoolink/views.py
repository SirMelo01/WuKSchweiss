from django.shortcuts import get_object_or_404, render, redirect
from yoolink.ycms.models import FAQ, UserSettings, Message, Product, TextContent, fileentry, Galerie, GaleryImage
import datetime
from django.http import HttpResponseRedirect


def load_index(request):
    faq = FAQ.objects.all()

    context = {
        'FAQ': faq,
    }
    
    reduced_products = Product.objects.filter(is_reduced=True)
    if reduced_products.exists():
        products = reduced_products[:3]
    else:
        products = Product.objects.all()[:3]

    context["products"] = products

    # Hero
    if TextContent.objects.filter(name="main_hero").exists():
        context["heroText"] = TextContent.objects.get(name='main_hero')

    # Dienstleistungen        
    if TextContent.objects.filter(name="main_dienstleistungen").exists():
        context["dienstText"] = TextContent.objects.get(name='main_dienstleistungen')

    if TextContent.objects.filter(name="main_dienst_1").exists():
        context["dienst1Text"] = TextContent.objects.get(name='main_dienst_1')
        
    if TextContent.objects.filter(name="main_dienst_2").exists():
        context["dienst2Text"] = TextContent.objects.get(name='main_dienst_2')
        
    if TextContent.objects.filter(name="main_dienst_3").exists():
        context["dienst3Text"] = TextContent.objects.get(name='main_dienst_3')
        
    if TextContent.objects.filter(name="main_dienst_4").exists():
        context["dienst4Text"] = TextContent.objects.get(name='main_dienst_4')
        
    # Angebote
    if TextContent.objects.filter(name="main_angebote").exists():
        context["angeboteText"] = TextContent.objects.get(name='main_angebote')
        
    # Angebote
    if TextContent.objects.filter(name="main_contact").exists():
        context["contactText"] = TextContent.objects.get(name='main_contact')
    
    # Images
    if fileentry.objects.filter(place='main_hero').exists():
        context["heroImage"] = fileentry.objects.get(place='main_hero')
        
    if fileentry.objects.filter(place='main_flow').exists():
        context["flowImage"] = fileentry.objects.get(place='main_flow')

    context["user_settings"] = UserSettings.objects.filter(user__is_staff=False).first()


    return render(request, 'pages/index.html', context=context)

def shop(request):
   return render(request, 'pages/shop.html', context={"products": Product.objects.filter(is_active=True)})

def detail(request, product_id):
     product = get_object_or_404(Product, id=product_id)
     return render(request, 'pages/detail.html', context={"product": product})
