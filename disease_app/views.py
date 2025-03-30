from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeafImageForm
from .models import LeafImage, PlantDisease
from .utils import predict_disease

def home_view(request):
    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            leaf_image = form.save()
            
            # Process the image and get prediction
            image_bytes = leaf_image.image.read()
            disease_name = predict_disease(image_bytes)
            
            # Find corresponding disease in database
            try:
                disease = PlantDisease.objects.get(name=disease_name)
                leaf_image.result = disease
                leaf_image.save()
            except PlantDisease.DoesNotExist:
                # Handle case where prediction doesn't match any disease in DB
                pass
            
            return redirect('disease_app:result', image_id=leaf_image.id)
    else:
        form = LeafImageForm()
    
    return render(request, 'disease_app/home.html', {'form': form})

def result_view(request, image_id):
    leaf_image = get_object_or_404(LeafImage, id=image_id)
    context = {
        'leaf_image': leaf_image,
    }
    return render(request, 'disease_app/result.html', context)