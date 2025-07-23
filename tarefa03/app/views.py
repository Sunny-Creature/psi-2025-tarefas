from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def usuarios(request):
    user_list = [
        {"nome": "Computador Ferreira Andrade", "matricula": "1234321", "idade": 12, "cidade": "Acari"},
        {"nome": "Microfone Oliveira da Silva", "matricula": "5678765", "idade": 19, "cidade": "Peruibe"},
        {"nome": "Impressora Eliany Costas", "matricula": "9012109", "idade": 20, "cidade": "San Francisco"},
        {"nome": "Maria Windows do Santos", "matricula": "", "idade": 15, "cidade": "Nova Iorque"},
        {"nome": "Linux Nascimento do Santos", "matricula": "1234321", "idade": 23, "cidade": "Nova Iorque"}
    ]

    context = {
        "usuarios": user_list,
    }
    
    return render(request, 'usuarios.html', context)