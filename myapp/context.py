from .models import Product

def ContextProcessors(request):
    return {
        'products': Product.objects.all()
    }
