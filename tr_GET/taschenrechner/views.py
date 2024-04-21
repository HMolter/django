from django.shortcuts import render

# Create your views here.
def taschenrechner(request):
    
    # Daten aus dem Formular
    if request.method == 'GET' and 'Taste' in request.GET:
        # die Werte aus dem Formular einlesen
        ans = int(request.GET[ 'ANS' ])
        key = int(request.GET[ 'Taste' ])

        anzeige = key
        if ans != 0:
            ans = ans + key
        else:
            ans = key

    elif request.method == 'GET' and 'oprtn' in request.GET:
        # die Werte aus dem Formular einlesen
        ans = int(request.GET[ 'ANS' ])
        action = request.GET[ 'oprtn' ]
        if action == "delete":
            anzeige = 0
            ans = 0
        elif action == "execute":
            anzeige = ans
            ans = 0
        elif action == "add":
            anzeige = "+"
    
    else:
        anzeige = 0
        ans = 0

    # Seite aufrufen und die Werte mitgeben    
    return render(request, 'taschenrechner/start.html', {'ans': ans, 'anzeige': anzeige})
