from django.shortcuts import render
def index(request):
    context = {
        'full_name': 'Noor Sufyan Aljourani',
        'student_id': '220220204',
        'address': 'Gaza, Palestine',
        'email': 'nooraljouranie@gmail.com',
        'major': 'Software Development',
        'university': 'Islamic University of Gaza',

    }
    return render(request, 'pages/index.html', context)
