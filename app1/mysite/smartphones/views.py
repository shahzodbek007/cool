from django.http import HttpResponse


def smartphones(request):
    html = "<h2>Smartphones</h2>"
    html += """
    <br>
    <ul>
    <li><b>Brand:</b> <a href = "http://127.0.0.1:8000/smartphones/samsung"> Samsung</a>
     <a href = "http://127.0.0.1:8000/smartphones/apple"> Apple</a></li>
     <li><a href ="http://127.0.0.1:8000/"> Home Products</a></li>
    </ul>
    """
    return HttpResponse(html)


def samsung(request):
    html = "<h1>Samsung</h1>"
    html += """
    <br>
    <ul>
    <li><Font size=4><b>Model:</b></font>Samsung A52</li>
    <li><Font size=4><b>Memory card:</b></font>4/128GB</li>
    <li><Font size=4><b>Color:</b></font>White</li>
    <li><a href ="https://www.mobezone.com/wp-content/uploads/2021/03/Samsung-Galaxy-A52.jpg">Photo</a></li>
    <li> <a href = "http://127.0.0.1:8000/smartphones/"> Home Page</a></li>
    </ul>
    """
    return HttpResponse(html)


def apple(request):
    html = "<h1>Apple</h1>"
    html += """
    <br>
    <ul>
    <li><Font size=5><b>Model:</b></font>Apple 12 Pro Max</li>
    <li><Font size=5><b>Memory card:</b></font>6/256GB</li>
    <li><Font size=5><b>Color:</b></font>Blue</li>
    <li><a href ="https://i0.wp.com/www.goodiegiveaways.co.uk/wp-content/uploads/2020/11/Win-an-Apple-iPhone.jpg">
     Photo</a></li>
     <li> <a href = "http://127.0.0.1:8000/smartphones/"> Home Page</a></li>
    </ul>
    """
    return HttpResponse(html)