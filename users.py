# Obviamente, essa não é a maneira ideal de manter os dados de login, mas isto é só um protótipo.

# No objeto usuários, o valor armazena o nome do usuário, a chave é um array, onde o elemento 0 é a senha
# E o elemento 1 é o privilégio.

# 'a' para atendente
# 'v' para veterinário

usuarios = {
    'yasmin.vitoria':['1234', 'a'],
    'aline.takahashi':['1234', 'v'],
    'amanda.santos':['1234', 'v'],
    'leticia.franca':['1234','v']
}

def valida_login(user, senha):
    username = usuarios[user]
    if username:
        if username[0]==senha:
            return
        return 'Senha Incorreta'
    return 'Usuário não existe'
    