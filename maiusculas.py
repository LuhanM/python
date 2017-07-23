class Maiusculas:
    def get_maiusculas(self, frase):
        result = ''
        for i in range(len(frase)):
            if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
                result += frase[i]
        return result