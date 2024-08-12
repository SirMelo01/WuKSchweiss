from django.shortcuts import get_object_or_404, render, redirect
from yoolink.ycms.models import FAQ, UserSettings, Message, Product, OpeningHours, TextContent, fileentry, Galerie, GaleryImage
import datetime
from django.http import HttpResponseRedirect

def get_opening_hours():
    opening_hours = {}
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    for day in days:
        if OpeningHours.objects.filter(day=day).exists():
            opening_hours[f"opening_{day.lower()}"] = OpeningHours.objects.get(day=day)
        else:
            opening_hours[f"opening_{day.lower()}"] = None
            
    user_settings = UserSettings.objects.filter(user__is_staff=False)
    if user_settings.exists():
        user_settings = user_settings.first()
        opening_hours["owner_data"] = user_settings
    return opening_hours

def load_index(request):
    faq = FAQ.objects.all()

    context = {
        'FAQ': faq,
    }
    
    reduced_products = Product.objects.filter(is_reduced=True, is_active=True)
    if reduced_products.exists():
        products = reduced_products[:3]
    else:
        products = Product.objects.filter(is_active=True)[:3]

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
    
    # Workflow
    if TextContent.objects.filter(name="main_flow_1").exists():
        context["flowText1"] = TextContent.objects.get(name='main_flow_1')

    if TextContent.objects.filter(name="main_flow_2").exists():
        context["flowText2"] = TextContent.objects.get(name='main_flow_2')

    if TextContent.objects.filter(name="main_flow_3").exists():
        context["flowText3"] = TextContent.objects.get(name='main_flow_3')

    if TextContent.objects.filter(name="main_flow_4").exists():
        context["flowText4"] = TextContent.objects.get(name='main_flow_4')

    if TextContent.objects.filter(name="main_flow_end").exists():
        context["flowTextEnd"] = TextContent.objects.get(name='main_flow_end')
    

    # Images
    if fileentry.objects.filter(place='main_hero').exists():
        context["heroImage"] = fileentry.objects.get(place='main_hero')
        
    if fileentry.objects.filter(place='main_flow').exists():
        context["flowImage"] = fileentry.objects.get(place='main_flow')

    context["user_settings"] = UserSettings.objects.filter(user__is_staff=False).first() 
    context.update(get_opening_hours())
    return render(request, 'pages/index.html', context=context)

def team(request):
    context = {}

    # Galerie
    if Galerie.objects.filter(place='team_galery').exists():
        context["teamGalery"] = Galerie.objects.get(place='team_galery').images.all()

    # Images
    if fileentry.objects.filter(place='team_hero').exists():
        context["heroImage"] = fileentry.objects.get(place='team_hero')

    # Hero Text
    if TextContent.objects.filter(name="team_hero").exists():
        context["heroText"] = TextContent.objects.get(name='team_hero')

    # Team Text
    if TextContent.objects.filter(name="team_team").exists():
        context["teamText"] = TextContent.objects.get(name='team_team')
    context.update(get_opening_hours())
    return render(request, 'pages/team.html', context)

def shop(request):
   context={"products": Product.objects.filter(is_active=True)}
   context.update(get_opening_hours())
   return render(request, 'pages/shop.html', context)

def detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)
    last_url = request.META.get('HTTP_REFERER')
    if not product.is_active:
        return render(request, "pages/errors/error.html", {
            "error": "Dieses Produkt ist nicht mehr verfügbar",
            "saveLink": last_url if last_url else '/'
        })
    context={"product": product}
    context.update(get_opening_hours())
    return render(request, 'pages/detail.html', context)

def impressum(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/impressum.html', context)

def datenschutz(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/datenschutz.html', context)

def cookies(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/cookies.html', context)
