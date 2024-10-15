from django.shortcuts import render, redirect, reverse
from .models import Car, CarComments
from django.contrib.auth.models import User


def edit_commit(request, commit_id):
    try:
        select_commit = CarComments.objects.get(pk=commit_id)
        if request.method == 'POST':
            if request.POST.get('edit_commit'):
                select_commit.comment = request.POST.get('description')
                select_commit.save()
                return redirect('car_info', CarComments.objects.get(id=commit_id).car.id)
            elif request.POST.get('delete_commit'):
                car_id = CarComments.objects.get(id=commit_id).car.id
                select_commit.delete()
                return redirect('car_info', car_id=car_id)
    except Exception as e:
        car = CarComments.objects.get(id=commit_id).car.id
        return redirect('car_info', car)
    return render(request, 'cars/edit_commit.html', {'commit': select_commit})


def commit(request, car_id):
    try:
        select_commit = CarComments.objects.get(id=request.POST.get('commit_id'))
        if request.POST.get('delete_commit'):
            select_commit.delete()
        elif request.POST.get('edit_commit'):
            return render(request, 'cars/edit_commit.html', {'commit': select_commit})
        return redirect('car_info', car_id)
    except CarComments.DoesNotExist:
        pass


def send(request, car_id, author_id, commit):
    new_comment = CarComments()
    new_comment.car = Car.objects.get(id=car_id)
    new_comment.author = User.objects.get(id=author_id)
    new_comment.comment = commit
    new_comment.save()
    return redirect('car_info', car_id=car_id)


def car_info(request, car_id):
    selected_car = Car.objects.get(id=car_id)
    description_comment = 'Комментарий к атомобилю'
    if request.method == 'POST':
        if 'delete_commit' in request.POST or 'edit_commit' in request.POST:
            try:
                select_commit = CarComments.objects.get(id=request.POST.get('commit_id'))
                if request.POST.get('delete_commit'):
                    select_commit.delete()
                elif request.POST.get('edit_commit'):
                    return redirect('edit_commit', select_commit.id)
                return redirect('car_info', car_id)
            except CarComments.DoesNotExist:
                print('Пытается вывести коментарий, которого уже нет')
        else:
            try:
                if request.POST.get('send'):
                    if request.POST.get('comment'):
                        return redirect('car_commit_send', car_id=car_id,
                                        author_id=request.user.id, commit=request.POST.get('comment'))
                    else:
                        return Exception
                elif request.POST.get('delete'):
                    car = Car.objects.get(pk=car_id)
                    car.delete()
                    return redirect('home', car_id)

                elif request.POST.get('edit'):
                    return redirect('car_update', car_id)
            except Exception as e:
                description_comment = 'Чтобы отправить коментарий ты должен что-нибудь написать!'

    comments = CarComments.objects.filter(car=selected_car).all()
    context = {
        'car': selected_car,
        'comments': comments,
        'description_comment': description_comment,
    }
    return render(request, 'cars/info.html', context)


def check_input_on_form(request):
    errors = []
    if not request.POST.get('description'):
        errors.append('Укажите описание машины!')
    if not request.POST.get('make'):
        errors.append('Укажите описание машины!')
    if not request.POST.get('model'):
        errors.append('Укажите описание машины!')
    elif request.POST.get('year') and len(request.POST.get('year')) != 4:
        errors.append('Не верно указан год выпуска машины!')
    return errors


def car_create(request):
    context = {'function': 'add_car',
               'function_name': 'Добавить'}
    if request.method == 'POST' and request.POST.get('add_car'):
        if errors := check_input_on_form(request):
            context['errors'] = errors
            return render(request, 'cars/car_create_or_edit.html', context)
        else:
            new_car = Car()
            new_car.make = request.POST.get('make')
            new_car.model = request.POST.get('model')
            new_car.year = request.POST.get('year')
            new_car.owner = User.objects.get(id=request.POST.get('user_id'))
            new_car.description = request.POST.get('description')
            new_car.save()
            return redirect('/')

    return render(request, 'cars/car_create_or_edit.html', context)


def car_update(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {'function': 'update_car',
               'function_name': 'Обновить',
               'make': car.make,
               'model': car.model,
               'year': car.year,
               'description': car.description}
    if request.method == 'POST' and request.POST.get('update_car'):
        if errors := check_input_on_form(request):
            context['errors'] = errors
            return render(request, 'cars/car_create_or_edit.html', context)
        else:
            car.make = request.POST.get('make')
            car.model = request.POST.get('model')
            car.year = request.POST.get('year')
            car.description = request.POST.get('description')
            car.save()
            return redirect('car_info', car_id)

    return render(request, 'cars/car_create_or_edit.html', context)
