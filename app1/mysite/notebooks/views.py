from django.http import HttpResponse


def notebooks(request):
    html = "<h2>Notebooks</h2>"
    html += """
    <br>
    <br>
    <ul>
    <li><b>Brand:</b></li>
    <li><a href ="http://127.0.0.1:8000/notebooks/asus"> Asus</a></li>
    <li><a href ="http://127.0.0.1:8000/notebooks/acer"> Acer</a></li>
    <li><a href ="http://127.0.0.1:8000/"> Home Products</a></li>
    </ul>
    """
    return HttpResponse(html)


def asus(request):
    html = "<h1>Asus</h1>"
    html += """
    <br>
    <ul>
    <li><Font size=4><b>Model:</b></font>Asus Core I7</li>
    <li><Font size=4><b>Ram:</b></font>8GB</li>
    <li><Font size=4><b>Color:</b></font>Black</li>
    <li><a href ="https://static.pleer.ru/i/p/806658/806658m.jpg">Photo</a></li>
    <li><a href ="http://127.0.0.1:8000/notebooks/">Home page</a></li>
    </ul>
    """
    return HttpResponse(html)


def acer(request):
    html = "<h1>Acer</h1>"
    html += """
    <br>
    <ul>
    <li><Font size=4><b>Model:</b></font>Acer Core I3</li>
    <li><Font size=4><b>Ram:</b></font>4GB</li>
    <li><Font size=4><b>Color:</b></font>Black</li>
    <li><a href ="https://im0-tub-ru.yandex.net/i?id=2488ed431d121e70b396789d1ef23beb-l&amp;n=13">Photo</a></li>
    <li><a href ="http://127.0.0.1:8000/notebooks/">Home page</a></li>
    </ul>
    """
    return HttpResponse(html)

