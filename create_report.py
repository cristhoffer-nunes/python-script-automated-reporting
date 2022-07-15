from fpdf import FPDF
from datetime import datetime
import os.path
import os

dateTimeObj = datetime.now()
ano = dateTimeObj.year
mes = dateTimeObj.month
dia = dateTimeObj.day

WIDTH = 210
HEIGHT = 297

def create_title(pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(80)
    pdf.write(5, f'Relatório Diário TrendFoods')
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{dia}/{mes}/{ano}')
    pdf.ln(17)


def report():
    pdf = FPDF()

    pdf.add_page()
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_letterhead.png", 0, 0, WIDTH)
    create_title(pdf)

    filename="Relatório.pdf"

    '''Second Page'''

    pdf.set_font('Arial', '', 14)

    pdf.write(5, f'Alertas de Falhas')
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_alertas.png", 15, 123, 115)
    pdf.ln(93)

    pdf.set_font('Arial', '', 14)

    '''Situational Page'''
    x = 2


    '''Third Page'''
    pdf.add_page()
    pdf.write(5, f'{x}.0 Painel')
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_alertas.png", 1, 18, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_microsservicos_acima_5_erro.png", 104, 18, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_container_parado.png", 1, 88, WIDTH / 2.05)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_container_reiniciado_recentemente.png", 104, 88, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_container_execucao.png", 1, 156, WIDTH / 2.05)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_memoria.png", 104, 156, WIDTH / 2.05)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_cpu.png", 1, 224, WIDTH / 2.05)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_disco.png", 104, 224, WIDTH / 2)

    '''Fourth Page'''
    pdf.add_page()
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_network.png", 1, 10, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_checkout_vs_pedidos.png", 104, 10, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_taxa_ecommerce.png", 1, 80, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_percentual_checkout_pedidos.png", 104, 80, WIDTH / 2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_media_pedidos_7d.png", 1, 150, WIDTH / 2.05, )
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_media_acessos_7d.png", 104, 150, WIDTH/2)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_qtd_requicoes_sse.png", 1, 220, WIDTH / 2.05)
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_falha_na_finalizacao_pedido.png", 104, 220, WIDTH / 2)
    

    '''Fifth Page'''
    pdf.add_page()

    pdf.link(65, 250, 75,75, "mailto:suporte@jbq.global")
    pdf.image(os.path.dirname(os.path.abspath(__file__)) + "/images/img_assinatura.png", 65, 250, 85)

    pdf.output(filename)