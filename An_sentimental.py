# Importamos las Bibliotecas que nos van a ayudar a realizar
# el analisis sentimental
import docx
from textblob import TextBlob

# Utilizarmos Object oriented programing para poder realizar
# el analisis replicando el mismo codigo en diferentes objetos (Corpus)
# Definimos una clase la cual se llamara Analisis_Sentimental

class Analisis_Sentimental():

    def __init__(self, Nombre_documento, direccion_documento):
        """Inicializar las funciones y parametros basicos"""

        self.direccion_documento = direccion_documento
        self.Nombre = Nombre_documento
        self.Nombre_documento = docx.Document(self.direccion_documento)
        self.y = 0.0
        self.texto_completo = []

    #Definimos una funcion que sera la encargada de leer los documentos
    def Leer_Documentos(self):
        """Función destinada a leer los parafos"""

        for parrafo in self.Nombre_documento.paragraphs:

            self.texto_completo.append(parrafo.text)

        return self.texto_completo

    def analisis_texto(self):
        """Función destinada a generar el análisis"""

        analisis = self.Leer_Documentos()

        analisis = str(analisis)

        blob = TextBlob(analisis)

        for sentence in blob.sentences:
           x = sentence.sentiment.polarity
           self.y += x


    def resultados(self):
        """Imprimir los resultados en la pantalla"""

        if self.y < 0 :

            print("\n---------------------------------------------------------------------"
                    f"\n El valor sentimental del {self.Nombre}  es: {self.y},"
                    "\npor lo tanto el comunicado tiene un tono Dovish"
                    "\n---------------------------------------------------------------------\n")
        elif self.y >0 :

            print("\n---------------------------------------------------------------------"
                    f"\n El valor sentimental del {self.Nombre}  es: {self.y},"
                    "\npor lo tanto el comunicado tiene un tono Hawkish"
                    "\n---------------------------------------------------------------------\n")

        elif self.y == 0:

            print("\n---------------------------------------------------------------------"
                    f"\n El valor sentimental del {self.Nombre}  es: {self.y},"
                    "\npor lo tanto el comunicado tiene un tono Neutro"
                    "\n---------------------------------------------------------------------\n")


if __name__ == "__main__":
    print('\n########################################### Minuta de la FED Enero 28, 2020 ##########################################')

    Minuta_FOMC_280120_S1 = Analisis_Sentimental("Segmento de Economic Situation de Minuta de 28/01/20",
        "280120_FOMC_EconS.docx")
    Minuta_FOMC_280120_S1.analisis_texto()
    Minuta_FOMC_280120_S1.resultados()

    Minuta_FOMC_280120_S2 = Analisis_Sentimental("Segmento de Finacial Situation de Minuta de 28/01/20",
        "280120_FOMC_FINA.docx")
    Minuta_FOMC_280120_S2.analisis_texto()
    Minuta_FOMC_280120_S2.resultados()

    Minuta_FOMC_280120_S3 = Analisis_Sentimental("Segmento de Economic Outlook de Minuta de 28/01/20",
        "280120_FOMC_EconO.docx")
    Minuta_FOMC_280120_S3.analisis_texto()
    Minuta_FOMC_280120_S3.resultados()

    print('########################################### Minuta de la FED Diciembre 10, 2019 ##########################################')

    Minuta_FOMC_101219_S1 = Analisis_Sentimental("Segmento de Economic Situation de Minuta de 10/12/19",
        "101219_FOMC_EconS.docx")
    Minuta_FOMC_101219_S1.analisis_texto()
    Minuta_FOMC_101219_S1.resultados()

    Minuta_FOMC_101219_S2 = Analisis_Sentimental("Segmento de Finacial Situation de Minuta de 10/12/19",
        "101219_FOMC_FINA.docx")
    Minuta_FOMC_101219_S2.analisis_texto()
    Minuta_FOMC_101219_S2.resultados()

    Minuta_FOMC_101219_S3 = Analisis_Sentimental("Segmento de Economic Outlook de Minuta de 10/12/19",
        "101219_FOMC_EconO.docx")
    Minuta_FOMC_101219_S3.analisis_texto()
    Minuta_FOMC_101219_S3.resultados()

    print('########################################### Minuta de la FED Octubre 29, 2019 ##########################################')

    Minuta_FOMC_291019_S1 = Analisis_Sentimental("Segmento de Economic Situation de Minuta de 29/10/19",
        "291019_FOMC_EconS.docx")
    Minuta_FOMC_291019_S1.analisis_texto()
    Minuta_FOMC_291019_S1.resultados()

    Minuta_FOMC_291019_S2 = Analisis_Sentimental("Segmento de Finacial Situation de Minuta de 29/10/19",
        "291019_FOMC_FINA.docx")
    Minuta_FOMC_291019_S2.analisis_texto()
    Minuta_FOMC_291019_S2.resultados()

    Minuta_FOMC_291019_S3 = Analisis_Sentimental("Segmento de Economic Outlook de Minuta de 29/10/19",
        "291019_FOMC_EconO.docx")
    Minuta_FOMC_291019_S3.analisis_texto()
    Minuta_FOMC_291019_S3.resultados()

    print('########################################### Comunicado de la FED Marzo 15, 2020 ##########################################')

    Comunicado_FOMC_150320 = Analisis_Sentimental("Comunicado sobre POLMO del 15/03/20.",
        "150320_FOMC_Com.S1.docx")
    Comunicado_FOMC_150320.analisis_texto()
    Comunicado_FOMC_150320.resultados()
