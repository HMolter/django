from django.shortcuts import render

# Create your views here.
def taschenrechner(request):
    
    # Daten aus dem Formular
    if request.method == 'POST' and 'Taste' in request.POST:
        # die Werte aus dem Formular einlesen
        ans = int(request.POST[ 'ANS' ])
        key = int(request.POST[ 'Taste' ])

        anzeige = key
        if ans != 0:
            ans = ans + key
        else:
            ans = key

    elif request.method == 'POST' and 'oprtn' in request.POST:
        # die Werte aus dem Formular einlesen
        ans = int(request.POST[ 'ANS' ])
        action = request.POST[ 'oprtn' ]
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
