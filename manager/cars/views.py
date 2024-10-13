from django.shortcuts import render
from .models import Car, CarComments


def car_info(request, car_id):
    selected_car = Car.objects.get(id=car_id)
    description_comment = 'Комментарий к атомобилю'
    if request.method == 'POST':
        if request.POST.get('send') == 'Опубликовать':
            if request.POST.get('comment'):
                new_comment = CarComments()
                new_comment.car_id = car_id
                new_comment.author = request.user
                new_comment.comment = request.POST.get('comment')
                new_comment.save()
            else: description_comment = 'Чтобы отправить коментарий ты должен что-нибудь написать!'
    comments = CarComments.objects.filter(car=selected_car).all()
    context = {
        'car': selected_car,
        'comments': comments,
        'description_comment': description_comment,
    }
    return render(request, 'cars/info.html', context)
