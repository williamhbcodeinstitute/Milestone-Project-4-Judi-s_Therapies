from django.shortcuts import render, redirect, reverse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing inside your shopping bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HG5d7BKRE4Q12M56b9YpHbgFfgE7oFCtPDkZhU4ZpoMVNGp14wt6z9r36vJ5IgXuDuRUjTC6F42RcowAPYdBFjD00idKRNaXc'
    }

    return render(request, template, context)
