from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from cart.models import Cart
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):

    # Retrieve cart data
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    for cart_item in cart_items:
        cart_item.item_total_price = cart_item.product.price * cart_item.quantity

    total_price = sum(item.product.price *
                      item.quantity for item in cart_items)

    total_price_in_cents = int(total_price * 100)

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=total_price_in_cents,  # amount in cents
                currency='usd',
                description='Example charge',
                source=token,
            )

            # Store order information in your database
            order = Order.objects.create(
                user=request.user,
                amount=total_price,
                charge_id=charge.id,
            )

            # Retrieve cart items
            cart_items = Cart.objects.filter(user=user)

            # Store each cart item in the order
            for item in cart_items:
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            # Clear the cart after successful payment
            cart_items.delete()

        except stripe.error.CardError as e:
            # Display error message to the user
            return render(request, 'checkout.html', {'error': e.error.message})

        # Payment successful, redirect to a success page
        return redirect('home')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_price_in_cents': total_price_in_cents,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }

    return render(request, 'checkout.html', context)
