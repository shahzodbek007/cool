from django.http import HttpResponse


def products(request):
    html = "<h1>Products</h1>"
    html += """
    <br>
    <ul>
    <li><a href ="http://127.0.0.1:8000/notebooks/">Notebooks</a></li>
    <li><a href ="http://127.0.0.1:8000/smartphones/">Smart Phones</a></li>
    <li><a href ="http://127.0.0.1:8000/monitors/">Monitors</a></li>
    </ul>
    """
    return HttpResponse(html)
