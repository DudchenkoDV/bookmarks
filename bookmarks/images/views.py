from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # Заполняем форму
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Данные в форме валидны
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # Перенаправит к закладке
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})
