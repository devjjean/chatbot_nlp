# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')  # Pega a mensagem do usuário
        response_message = process_message(user_message)  # Processa a resposta
        return JsonResponse({'response': response_message})  # Retorna a resposta como JSON
    return render(request, 'chatbot/chat.html')  # Renderiza o template HTML

def process_message(message):
    message = message.lower().strip()
    
    responses = {
        "qual é o seu nome?": "Eu sou o Chatbot, como posso ajudar você?",
        "o que você pode fazer?": "Posso responder perguntas e ajudar com informações básicas.",
        "qual é a sua idade?": "Eu sou um programa de computador, então não tenho idade.",
        "como você funciona?": "Eu uso regras simples para responder perguntas. Se precisar de algo mais complexo, posso precisar de ajuda externa.",
        # Adicionando variações
        "qual o seu nome?": "Eu sou o Chatbot, como posso ajudar você?",
        "o que faz?": "Posso responder perguntas e ajudar com informações básicas.",
        "idade": "Eu sou um programa de computador, então não tenho idade.",
        "como funciona?": "Eu uso regras simples para responder perguntas. Se precisar de algo mais complexo, posso precisar de ajuda externa.",
        "oi": "Olá! Como posso ajudar você hoje?",
        "olá": "Oi! Em que posso ajudar?",
        "bom dia": "Bom dia! Como posso ajudar você?",
        "boa tarde": "Boa tarde! O que você precisa?",
        "boa noite": "Boa noite! Como posso ajudar?",
        "ajuda": "Estou aqui para ajudar! Qual é a sua dúvida?",
    }
    
    # Retorna a resposta correspondente ou uma resposta padrão se não houver correspondência
    return responses.get(message, "Desculpe, não entendi sua pergunta. Pode reformular?")