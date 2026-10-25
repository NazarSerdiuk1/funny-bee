from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Order, OrderItem

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        if len(cart) == 0:
            return redirect('cart:cart_detail')

        # Створюємо замовлення на основі даних з форми у кошику
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            delivery_method=request.POST.get('delivery_method'),
            payment_method=request.POST.get('payment_method'),
            comment=request.POST.get('comment'),
            user=request.user if request.user.is_authenticated else None
        )
        # Переносимо товари з сесії кошика в моделі OrderItem
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
            
        # Очищуємо сесію кошика після успішного замовлення
        cart.clear()
        
        context = {
            'order': order,
        }
        return render(request, 'orders/order_success.html', context)
        
    return redirect('cart:cart_detail')