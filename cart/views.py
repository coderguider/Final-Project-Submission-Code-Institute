from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")
    
    
def add_to_cart(request, item_id):
    """Add a quantity of the specified featrue to the cart"""
    quantity = 1
    
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, quantity)
    
    request.session['cart'] = cart
    return redirect('features')
    
    
def adjust_cart(request, item_id):
    """Adjust the quantity of the specified feature to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))