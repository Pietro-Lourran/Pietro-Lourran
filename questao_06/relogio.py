''' Imprime um horario em HH:MM:SS e mensagens de aviso caso valores sejam inválidos 
para a hora , minutos e segundo'''
class Relogio:
    def __init__(self, h, m, s):
        # Verifica se as horas são válidas
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.h = h
            self.m = m
            self.s = s
        else:
            print("Horario digitado invalido !")
            self.h = self.m = self.s = None

    def __str__(self):
        # Retorna o horário
        if self.h is None:
            return "Horário inválido"
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def total_segundos(self):
        # Converte para segundos
        return self.h * 3600 + self.m * 60 + self.s

    def __add__(self, outro):
        # Soma duas horas e retorna 
        total = self.total_segundos() + outro.total_segundos()
        h = (total // 3600) % 24
        m = (total % 3600) // 60
        s = total % 60
        return Relogio(h, m, s)

    def __sub__(self, outro):
        # Subtrai dois horários se o primeiro for maior ou igual
        if self.total_segundos() < outro.total_segundos():
            print("O primeiro horario dever ser maior ou igual ao segundo")
            return None
        total = self.total_segundos() - outro.total_segundos()
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return Relogio(h, m, s)

    def __eq__(self, outro):
        # confere se dois horários são iguais ou nao 
        return self.total_segundos() == outro.total_segundos()

    def __lt__(self, outro):
        # confere se este horário é menor que o outro
        return self.total_segundos() < outro.total_segundos()

    def __gt__(self, outro):
        # confere se este horário é maior que o outro
        return self.total_segundos() > outro.total_segundos()
