from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    html = "<h2>Hello Django!!!</h2>"
    html += """
    <br>
    <br>
    <ul>
    <li><a href ="http://127.0.0.1:8000/second/">Second Page</a></li>
    <li><a href ="http://127.0.0.1:8000/first/">First Name</a></li>
    <li><a href ="http://127.0.0.1:8000/last/">Last Name</a></li>
    <li><a href ="http://127.0.0.1:8000/books/">Books</a>
    </li>
    </ul>
    """
    return HttpResponse(html)


def page_second(request):
    html = "<h2>This is page!!!</h2>"
    html += """
        <br>
        <br>
        <ul>
        <li><a href ="http://127.0.0.1:8000/">Home Page</a></li>
        <li><a href ="http://127.0.0.1:8000/first/">First Name</a></li>
        <li><a href ="http://127.0.0.1:8000/last/">Last Name</a></li>
        <li><a href ="http://127.0.0.1:8000/books/">Books</a>
        </li>
        </ul>
        """
    return HttpResponse(html)


def first_name(request):
    html = "<h2>Valijonov</h2>"
    html += """
        <br>
        <br>
        <ul>
        <li><a href ="http://127.0.0.1:8000/">Home Page</a></li>
        <li><a href ="http://127.0.0.1:8000/second/">Second Page</a></li>
        <li><a href ="http://127.0.0.1:8000/last/">Last Name</a></li>
        <li><a href ="http://127.0.0.1:8000/books/">Books</a>
        </li>
        </ul>
        """
    return HttpResponse(html)


def last_name(request):
    html = "<i><h2>Shahzodbek</h2></i>"
    html += """
            <br>
            <br>
            <ul>
            <li><a href ="http://127.0.0.1:8000/">Home Page</a></li>
            <li><a href ="http://127.0.0.1:8000/second/">Second Page</a></li>
            <li><a href ="http://127.0.0.1:8000/first/">First Name</a></li>
            <li><a href ="http://127.0.0.1:8000/books/">Books</a>
            </li>
            </ul>
            """
    return HttpResponse(html)


# def user(request):
#     html = "<i><h2>Shahzodbek Valijonov</h2></i>"
#     html += """
#                 <br>
#                 <br>
#                 <ul>
#                 <li><a href ="http://127.0.0.1:8000/">Home Page</a></li>
#                 <li><a href ="http://127.0.0.1:8000/second/">Second Page</a></li>
#                 <li><a href ="http://127.0.0.1:8000/first/">First Name</a></li>
#                 <li><a href ="http://127.0.0.1:8000/last/">Last Name</a>
#                 <li><a href ="">User Name</a>
#                 </li>
#                 </ul>
#                 """
#     return HttpResponse(html)

