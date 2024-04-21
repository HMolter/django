from django.shortcuts import render

# Create your views here.
def taschenrechner(request):
    # Liste der Zahlentasten
    numkeys = [7,8,9,5,6,7,1,2,3]
    # Daten aus dem Formular
    if request.method == 'GET' and 'Taste' in request.GET:
        # die Werte aus dem Formular einlesen
        ans = int(request.GET[ 'ANS' ])
        key = int(request.GET[ 'Taste' ])

        anzeige = key
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
    else:
        anzeige = 0
        ans = 0

    # Seite aufrufen und die Werte mitgeben    
    return render(request, 'taschenrechner/start.html', {'ans': ans, 'anzeige': anzeige, 'numkeys': numkeys })

def addition(request):
    # Liste der Zahlentasten
    numkeys = [7,8,9,5,6,7,1,2,3]
    # Daten aus dem Formular
    ans = int(request.GET[ 'ANS' ])
    anzeige = ans
    
    if request.method == 'GET' and 'Taste' in request.GET:
        # die Werte aus dem Formular einlesen
        key = int(request.GET[ 'Taste' ])
        anzeige = key
        ans = ans + key

    # Seite aufrufen und die Werte mitgeben    
    return render(request, 'taschenrechner/add.html', {'ans': ans, 'anzeige': anzeige, 'numkeys': numkeys })
