from django.shortcuts import redirect, render
from .tasks import create_multiple_customer
from .models import Customer, Post

# Create your views here.

def generate_random_customers(request):
    if request.method == "POST":
        num_of_cust=request.POST.get('num_of_customer')
        customers=int(num_of_cust)
        create_multiple_customer.delay(customers)

        return redirect("customers")
    return render(request, "index.html")


def display_customers(request):
    customers = Customer.objects.all()
    context={
            'customers_list':customers
            }
    return render(request, "display.html", context)


def post_read_view(request, slug):
    post=Post.objects.get(slug=slug)
    context={
        'post':post
    }
    return render(request, "post.html", context)





