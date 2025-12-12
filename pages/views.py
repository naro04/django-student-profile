from django.shortcuts import render
from datetime import date
def index(request):
    context = {
        'full_name': 'noor',
        'last_name': ' aljourani',
        'student_id': 220220204,
        'address': 'Gaza, Palestine',
        'email': '', 
        'major': 'Software Development',
        'university': 'Islamic University of Gaza',
        'date_of_birth': date(2004, 2, 5), 
    }
    return render(request, 'pages/index.html', context)
