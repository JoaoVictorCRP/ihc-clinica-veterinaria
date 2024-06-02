# Obviamente, essa não é a maneira ideal de manter os dados de login, mas isto é só um protótipo.

# No objeto usuários, o valor armazena o nome do usuário, a chave é um array, onde o elemento 0 é a senha
# E o elemento 1 é o privilégio.

# 'a' para atendente
# 'v' para veterinário

usuarios = {
    'admin':['123', 'a'],
    'yasmin.vitoria':['123', 'a'],
    'aline.takahashi':['123', 'v'],
    'amanda.santos':['123', 'v'],
    'leticia.franca':['123','v']
}

for u in usuarios:
    print(usuarios[u][1])
    