from django.shortcuts import render, redirect
import json,requests, random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def prueba(request):
    return render(request, 'prueba.html')

def get_pokeinfo(poke_id):
    flavor_text = (json.loads((requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke_id}/')).content))['flavor_text_entries'][0]['flavor_text']
    name = (json.loads((requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}/')).content))['name']
    sprite = (json.loads((requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}/')).content))['sprites']['front_default']
    stats = (json.loads((requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}/')).content))['stats']
    return {'poke_flavor_text':flavor_text, 'poke_name':name, 'poke_id':poke_id, 'poke_sprite':sprite, 'poke_stats':stats}

def pokeLike(poke_id):
    pass

def menu(request):
    user = request.user
    poke_names = (json.loads((requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')).content))['name']
    if request.method == 'POST':
        search = request.POST.get('search')
        if search: poke_info=get_pokeinfo(search)
        else: poke_info = get_pokeinfo(random.randint(0,150))
    return render(request, 'menu.html', {'poke_info':poke_info, 'poke_names':poke_names})

@login_required(login_url='menu')
def profile(request):

    return render(request, 'profile.html')

