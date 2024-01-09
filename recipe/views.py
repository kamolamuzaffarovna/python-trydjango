from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm
from .models import Recipe, Tag, Ingredient
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


def recipe_list(request):

    tag = request.GET.get('tag')
    q= request.GET.get('q')
    q_condition = Q()
    if q:
        q_condition = Q(title__icontains=q)
    tag_condition = Q()
    if tag:
        tag_condition = Q(tags__title=tag)

    recipes = Recipe.objects.filter(q_condition, tag_condition).order_by('-id')
    paginator = Paginator(recipes, 1)
    page_number = request.GET.get('page')
    page_qs = paginator.get_page(page_number)

    context = {
         'object_list': page_qs
    }

    return render(request, 'recipe/index.html', context)


def my_recipe_list(request):

    tag = request.GET.get('tag')
    q = request.GET.get('q')
    q_condition = Q()
    if q:
        q_condition = Q(title__icontains=q)
    tag_condition = Q()
    if tag:
        tag_condition = Q(tags__title=tag)

    recipes = Recipe.objects.filter(q_condition, tag_condition).order_by('-id')

    context = {
         'object_list': recipes
    }

    return render(request, 'recipe/index.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    is_author_lookup = Q(is_active= True)
    if request.user == recipe.author:
        is_author_lookup = Q()
    ingredients = Ingredient.objects.filter(Q(recipe_id=recipe.id) & is_author_lookup)
    is_author = request.user == recipe.author
    context = {
         'object': recipe,
         'ingredients': ingredients,
         'is_author': is_author
    }
    return render(request, 'recipe/detail.html', context)



def recipe_create(request):
    if not request.user.is_authenticated:
        messages.info(request, "You should log in first.")
        reverse_url = reverse('auth:login') + "?next=" + request.path
        return redirect(reverse_url)
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.id
            obj.save()
            form.save_m2m()
            detail_url = reverse('recipe:detail', args=[obj.slug])
            return redirect(detail_url)

    context = {
        "form": form
    }
    return render(request, 'recipe/create.html', context)


def recipe_update(request, slug):
    instance = get_object_or_404(Recipe, slug=slug)
    form = RecipeForm(instance=instance)
    if request.method == 'POST':
        form = RecipeForm(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            detail_url = reverse('recipe:detail', kwargs={"slug": instance.slug})
            return redirect(detail_url)

    context = {
        'form': form,
        'header': "Recipe Update",
    }
    return render(request, 'recipe/create.html', context)

def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        if not request.user == recipe.author:
            messages.warning(request, "You have no enough permissions to delete ")
            return redirect(reverse('recipe:detail', args=[recipe.slug]))
        recipe.delete()
        return redirect('recipe:list')
    context = {
        'object': recipe
    }
    return render(request, 'recipe/delete.html', context)

def ingredient_create(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    reverse_url = reverse('recipe:detail', args=[recipe.slug])
    form = IngredientForm()
    if recipe.author != request.user:
        messages.error(request, 'You have no enough permissions')
        return redirect(reverse_url)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.recipe = recipe
            obj.save()
            messages.success(request, f'You create ingredient "{obj.title}".')
            return redirect(reverse_url)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'recipe/ingredient_create.html', context)

def recipe_ingredient_edit(request, slug, pk, *args, **kwargs):
    recipe = get_object_or_404(Recipe, slug=slug)
    reverse_url = reverse('recipe:detail', args=[slug])
    instance = get_object_or_404(Ingredient, id=pk)
    if instance not in recipe.ingredients.all():
        raise ObjectDoesNotExist(f"{instance.title} does not exist in {recipe.title} recipe")
    if recipe.author != request.user:
        messages.error(request, 'You have no enough permissions')
        return redirect(reverse_url)
    form = IngredientForm(instance=instance)
    if request.method == 'POST':
        form = IngredientForm(data=request.POST, instance=instance)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'You changed an ingredient "{obj.title}".')
            return redirect(reverse_url)
    context = {
        'form': form,
        'recipe': recipe,
        'title': "Change ingredient belong to "
    }
    return render(request, 'recipe/ingredient_create.html', context)

def recipe_ingredient_delete(request, *args, **kwargs):
    recipe = get_object_or_404(Recipe, slug=kwargs['slug'])
    reverse_url = reverse('recipe:detail', args=[kwargs['slug']])
    instance = get_object_or_404(Ingredient, id=kwargs['pk'])
    if instance not in recipe.ingredients.all():
        raise ObjectDoesNotExist(f"{instance.title} does not exist in {recipe.title} recipe")
    if recipe.author != request.user:
        messages.error(request, 'You have no enough permissions')
        return redirect(reverse_url)
    if request.method == 'POST':
        instance.delete()
        messages.error(request,f'"{instance.title} is deleted"')
        return redirect(reverse_url)
    context = {
         'recipe': recipe,
         'object': instance
     }
    return render(request, 'recipe/ingredient_delete.html', context)
