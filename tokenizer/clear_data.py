from unicodedata import normalize
import re
import string


class clear_data:
    
    @staticmethod
    def remove_accents(string_init):
        """

        @:param string_init String with accents:
        @:return: string_out String without accents;
        """
        try:
            string_partial = normalize('NFKD', texto)
        except Exception as e:
            string_out = string_in
            return string_out
        string_out =  re.sub(r'[^a-zA-Z0-9 \\]', '', string_partial)
        return string_out

    @staticmethod
    def remover_points(string_in):
        """
        @:param string_in: String with points
        @:return: string_out: String without points
        """
        for char in string.punctuation:
            string_partial = string_in.replace(char, ' ')
        string_out = re.sub(r'\s\s+', ' ', string_partial).strip()
        return string_out

    @staticmethod
    def clear_proccess(string_in):
        try:
            string_in = string_in.upper()
            string_partial = clear_data().remover_acentos(valor)
            valor = limpeza().remover_pontuacao(valor)
        finally:
            return valor
