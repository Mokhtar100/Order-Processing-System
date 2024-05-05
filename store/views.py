from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Order, OrderItem
from .forms import CheckoutForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings



def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(customer_name='Anonymous', email='anonymous@example.com', status='Pending')
    
    if product.stock <= 0:
        messages.error(request, f'Sorry, {product.name} is out of stock!')
        return redirect('product_list')
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, price=product.price, defaults={'quantity': 1})
    
    if not created:
        order_item.quantity += 1
        order_item.save()
    
    order.total_amount += product.price
    order.save()
    
    product.stock -= 1  
    product.save()
    
    messages.success(request, f'{product.name} added to your cart')
    return redirect('product_list')

def order_detail(request):
    order = Order.objects.filter(status='Pending').first()
    return render(request, 'store/order_detail.html', {'order': order})

def checkout(request):
    order = Order.objects.filter(status='Pending').first()
    if not order:
        messages.error(request, 'There are no pending orders to checkout.')
        return redirect('product_list')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            order.status = 'Paid'
            order.customer_name = name
            order.email = email
            order.save()
            send_order_confirmation_email(order)
            messages.success(request, 'Order placed successfully! Check your email for confirmation.')
            return render(request,'store/done.html')
    else:
        form = CheckoutForm()
    
    return render(request, 'store/checkout.html', {'form': form})




def send_order_confirmation_email(order):
    if order.email:
        subject = 'Order Confirmation'
        html_message = render_to_string('store/email/order_confirmation.html', {'order': order})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to_email = [order.email]
        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
    else:
        print("Order email is not provided.")


def done(request):
    return render('store/done.html')        