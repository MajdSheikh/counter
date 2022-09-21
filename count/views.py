from django.shortcuts import render, redirect

def root(request):
    if  'x' not in request.session['x']:
        request.session['x'] = 0
    else:
        request.session['x'] += 1
    return render(request, "index.html")
    


def destroy(request):
    del request.session['x']
    return redirect('/')
    

