from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from io import BytesIO


def compress_and_download(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        quality = int(request.POST['quality'])

        img = Image.open(image)
        compressed_image = BytesIO()
        img.save(compressed_image, format='JPEG', quality=quality)
        compressed_image.seek(0)

        response = HttpResponse(compressed_image.read(), content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename=compressed_image.jpg'
        return response

    return render(request, 'index.html')
