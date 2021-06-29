from django.http import HttpResponse


def monitors(request):
    html = "<h2>Monitors</h2>"
    html += """
        <br>
        <ul>
        <li> <a href = "http://127.0.0.1:8000/monitors/hp_monitor"> Hp</a></li>
        <li> <a href = "http://127.0.0.1:8000/monitors/dell_monitor"> Dell</a></li>
        <li><a href ="http://127.0.0.1:8000/"> Home Products</a></li>
        </ul>
        """
    return HttpResponse(html)


def hp_monitor(request):
    html = "<h2>Hp Monitor</h2>"
    html += """
        <br>
        <ul>
        <li> <a href = 
        "https://www.sferaufficio.com/immagini/http://images.icecat.biz/img/gallery/53130965_0867120977.jpg"> Hp</a></li>
        <li> <a href = "http://127.0.0.1:8000/monitors/"> Home Page</a></li>
        </ul>
        """
    return HttpResponse(html)


def dell_monitor(request):
    html = "<h2>Dell</h2>"
    html += """
        <br>
        <ul>
        <li> <a href = 
        "https://cdn.comfy.ua/media/catalog/product/cache/4/image/1440x1080/62defc7f46f3fbfc8afcd112227d1181/d/e/dell_u3219q_210-aquo_black.jpg"> Dell</a></li>
        <li> <a href = "http://127.0.0.1:8000/monitors/"> Home Page</a></li>
        </ul>
        """
    return HttpResponse(html)
