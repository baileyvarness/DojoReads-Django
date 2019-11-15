from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    print('request.POST: ', request.POST)
    errors = Users.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        # hash password
        hashed_password = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        new_user = Users.objects.create(name=request.POST['name'],
                                       alias=request.POST['alias'],
                                       email=request.POST['email'],
                                       password=hashed_password)
        if new_user:
            request.session['uid'] = new_user.id
        else:
            print('there was a problem creating the user')
            return redirect('/')

    return redirect('/books')


def login(request):
    user_list = Users.objects.filter(email=request.POST['email'])
    if len(user_list) > 0:
        hashed_password = user_list[0].password
        if bcrypt.checkpw(request.POST['password'].encode(), hashed_password.encode()):
            request.session['uid'] = user_list[0].id
            return redirect('/books')
        else:
            messages.error(request, 'invalid email and/or password')
    else:
        messages.error(request, 'invalid email and/or password')
    return redirect('/')

# THIS IS THE PAGE WITH ALL THE BOOKS AND REVIEWS
def books(request):
    if 'uid' not in request.session:
        print('we do not have a user id in session')
        return redirect('/')
    latest_three_reviews = Review.objects.all().order_by('-created_at')[:3]
    context = {
        'user': Users.objects.get(id=request.session['uid']),
        'book': Books.objects.all(),
        'reviews': Review.objects.all(),
        'latest_three_reviews': latest_three_reviews
    }
    return render(request, "books.html", context)

# THIS IS THE PAGE WITH THE FORM TO FILL IN ABOUT A NEW BOOK
def add_book(request):
    context = {
        'author': Authors.objects.all()
    }
    return render(request, "add_book.html", context)

# THIS IS THE ROUTE FOR THE POSTING OF THE NEW BOOK BEING ADDED
def book_being_added(request):
    if len(request.POST['new_author']) == 0:
            author = Authors.objects.get(id=request.POST['dropdown_authors'])
    else:
        author = Authors.objects.create(name=request.POST['new_author'])
    book = Books.objects.create(
        title=request.POST['title'], author=author)
    user = Users.objects.get(id=request.session['uid'])
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, user=user)
    return redirect(f'/books/{book.id}')

# THIS IS THE PAGE FOR ONE SPECIFIC BOOK
def one_book_page(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id),
        'reviews': Review.objects.all(),
        'user': Users.objects.get(id=request.session['uid'])
    }
    return render(request, "book_page.html", context)

def review_being_added(request, book_id):
    book = Books.objects.get(id=book_id)
    user = Users.objects.get(id=request.session['uid'])
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, user=user)
    return redirect(f'/books/{book.id}')

def user_profile(request, user_id):
    user = Users.objects.get(id=user_id)
    context = {
        'user': user,
        'count': len(user.review.all())
    }
    return render(request, "user.html", context)

def delete_review(request, book_id, review_id):
    review_to_delete = Review.objects.get(id=review_id)
    review_to_delete.delete()
    return redirect(f'/books/{book_id}')

def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out.")
    return redirect('/')