from django.http import HttpResponse


def books_genre(request):
    html = "<h2>Books</h2>"
    html += """
        <br>
        <br>
        <ul>
        <li><a href ="http://127.0.0.1:8000/books/list/">List</a></li>
        <li><a href ="http://127.0.0.1:8000/books/after/">After</a></li>
        <li><a href ="https://www.instagram.com/shahz0dboy/">My Instagram</a></li>
        <li><a href ="https://www.tiktok.com/@shahzod_a.u.e?">My Tiktok</a></li>
        <h1 align="right"> <font size=5>Mening ilovalarim: <li><a href ="https://www.instagram.com/shahz0dboy/">My Instagram</a></li></h1>  
        <h4 align="right"><li><a href ="https://www.tiktok.com/@shahzod_a.u.e?">My Tiktok</a></li></h4>
        </li>
        </ul>
        """
    return HttpResponse(html)


def books_list(request):
    html = "<h2>Kitoblar olamiga Xush kelibsiz</h2>"
    html += """
        <br>
        <br>
        <ul>
        <li><a href ="http://127.0.0.1:8000/books/after/">After</a></li>
        <li><a href ="http://127.0.0.1:8000/books/">Books</a>
        </li>
        </ul>
        """
    return HttpResponse(html)


def books_after(request):
    html = "<h2>Kitoblar Afterlari</h2>"
    html += """
        <br>
        <br>
        <ul>
        <li><a href ="http://127.0.0.1:8000/books/list/">List</a></li>
        <li><a href ="http://127.0.0.1:8000/books/">Books</a>
        </li>
        </ul>
        """
    return HttpResponse(html)

