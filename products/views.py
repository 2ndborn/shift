from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    num_reviews = reviews.count()
    review_score = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    context = {
        'product': product,
        'reviews': reviews,
        'num_reviews': num_reviews,
        'review_score': review_score,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to view this page')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to view this page')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to view this page')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))          
    product = get_object_or_404(Product, pk=product_id)
    user_profile = request.user.userprofile
    review, create = Review.objects.get_or_create(user=user_profile, product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'There was an error with your review.')
    else:
        form = ReviewForm(instance=review)    


@login_required
def edit_review(request, product_id, review_id):
    """ Edit a review of a product """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))          
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id, user=request.user.userprofile, product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'There was an error with your review.')
    else:
        form = ReviewForm(instance=review)

        context = {
            'form': form,
            'product': product
         }
         
    return render(request, 'products/edit_review.html', context)

@login_required
def delete_review(request, product_id, review_id):
    """ Delete a review of a product """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to login or register to view this page.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id, user=request.user.userprofile, product=product)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))   


def view_review(request, product_id):
    """ to view reviews """
    review = Review.objects.filter(product=product)
    num_reviews = reviews.count()
    review_score = Review.objects.aggregate(Avg('rating', default=0))
    context = {
        'reviews': reviews,
        'num_reviews': num_reviews,
        'review_score': review_score,
    }


def subscription(request):
    """A view to render the subscription page"""

    return render(request, 'products/subscription.html')
