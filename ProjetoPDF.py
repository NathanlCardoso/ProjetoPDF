# Projeto em python para PDF 
# Se atente em produzir em ambiente virtual (venv)


from fpdf import FPDF

class PDFChecklist(FPDF):
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
        
pdf = PDFChecklist()
pdf.add_page()

pdf.chapter_title("Checklist para Estação de Trabalho - Manutenção de Celulares")

# Substituindo travessões por hífen simples para evitar erro de encoding
texto_essencial = (
    "- Kit de chaves de precisão (Jakemy JM-8152 ou Yaxun YX-6028)\n"
    "- Espátulas metálicas e plásticas (2 ou 3 unidades)\n"
    "- Palhetas de nylon ou ABS\n"
    "- Ventosa forte\n"
    "- Pinças antiestáticas (reta e curvada)\n\n"

    "- Ferro de solda com controle de temperatura (Yaxun 936 ou Hikari HK-936)\n"
    "- Estação de ar quente (Yaxun 858D ou 878D+)\n"
    "- Suporte para ferro de solda com esponja de limpeza\n"
    "- Fio de solda fino (0.3mm ou 0.5mm) + pasta de solda\n\n"

    "- Multímetro digital (Minipa ET-1002 ou DT-830B)\n"
    "- Fonte assimétrica (opcional, mas recomendada) (Yaxun 1502D+)\n"
    "- Cabo de força de teste para celulares (alligator clip)\n\n"

    "- Álcool isopropílico 99% (mínimo 1 litro)\n"
    "- Pincéis antiestáticos e escovas macias\n"
    "- Fita Kapton\n"
    "- Panos de microfibra\n\n"

    "- Tapete de silicone antiestático com compartimentos\n"
    "- Pulseira antiestática (opcional)\n"
    "- Caixas ou organizadores para parafusos e peças"
)

texto_recomendado = (
    "- Lupa com iluminação ou microscópio USB\n"
    "- Estação de retrabalho avançada (2 em 1: ar quente + ferro de solda)\n"
    "- Máquina separadora de tela (para troca de vidro)\n"
    "- Balança de precisão e organizador magnético"
)

texto_estrutura = (
    "- Mesa resistente e espaçosa (mínimo 1 metro de largura)\n"
    "- Boa iluminação (luz branca, 6000K)\n"
    "- Cadeira confortável\n"
    "- Estante ou gaveteiro para armazenar peças e ferramentas\n"
    "- Estabilizador ou nobreak"
)

texto_investimento = (
    "- Kit de chaves + espátulas + palhetas: R$ 100 ~ R$ 200\n"
    "- Ferro de solda: R$ 120 ~ R$ 200\n"
    "- Estação de ar quente: R$ 300 ~ R$ 450\n"
    "- Multímetro digital: R$ 60 ~ R$ 150\n"
    "- Fonte assimétrica (opcional): R$ 250 ~ R$ 400\n"
    "- Limpeza e organização: R$ 100 ~ R$ 200\n"
    "- Tapete + organizadores: R$ 50 ~ R$ 120\n"
    "- TOTAL (básico): R$ 800 ~ R$ 1.200\n"
    "- TOTAL (completa): R$ 1.200 ~ R$ 2.000"
)

pdf.chapter_title("1. Ferramentas Essenciais")
pdf.chapter_body(texto_essencial)

pdf.chapter_title("2. Ferramentas Recomendadas")
pdf.chapter_body(texto_recomendado)

pdf.chapter_title("3. Estrutura da Estação de Trabalho")
pdf.chapter_body(texto_estrutura)

pdf.chapter_title("4. Investimento Inicial Estimado (Brasil - 2025)")
pdf.chapter_body(texto_investimento)

# se atente ao caminho da sua pasta!
pdf_path = "/caminho/da/sua/pagina/checklist.pdf"
pdf.output(pdf_path)

print(f"PDF gerado em: {pdf_path}")
