import streamlit as st

# Configuração da página
st.set_page_config(page_title="Resumo Profissional", layout="wide")

# Injeção de CSS para estilização
st.markdown("""
<style>
.stApp {
    background-color: #0E2F44;  /* Fundo em tom escuro */
}
.profile-pic {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin: auto;
    display: block;
}
h1, h3, h4, p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Exibição da foto de perfil
st.markdown(
    '<img src="https://media.licdn.com/dms/image/v2/D4D35AQGCBK9jx2iMtw/profile-framedphoto-shrink_200_200/profile-framedphoto-shrink_200_200/0/1730613262437?e=1742486400&v=beta&t=QBs3hfnhaSfdryiV7i-eIAK3nmS6CDgnFqPB4IV-LbA" class="profile-pic">',
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown('<h1 style="text-align: center;">Patrick Oliveira</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center;">Profissional da Tecnologia da Informação</h3>', unsafe_allow_html=True)

# Resumo Profissional (informações complementares do PDF)
resumo_texto = """
Olá, meu nome é **Patrick Oliveira**. Sou apaixonado por tecnologia e inovação, com sólida formação em *Gestão da Tecnologia da Informação* e comprometido com o aprimoramento contínuo.

Minha trajetória iniciou com o desenvolvimento de habilidades em suporte técnico e inspeção de qualidade, atuando em comunidades online de TI e, posteriormente, estagiando no setor de compras do Hospital Unimed Limeira – experiência que aprimorou minhas competências administrativas e operacionais.

Investi constantemente em qualificação, participando de cursos e treinamentos nas áreas de:
- **Inteligência Artificial e Computação em Nuvem**
- **Desenvolvimento e Segurança**
- **Gestão, Qualidade e Inovação**

Minhas competências englobam a configuração e manutenção de sistemas operacionais (Windows e Linux), processos de melhoria contínua, segurança de endpoints, gestão de riscos e análise de dados. Estou em busca do meu primeiro emprego na área de TI, onde poderei aplicar minhas habilidades e contribuir com soluções inovadoras. Vamos conversar sobre como posso agregar valor ao seu time?
"""

st.markdown(resumo_texto)

# Seções com informações detalhadas (dados complementares do PDF)
secoes = [
    {
        "titulo": "Experiência",
        "conteudo": """
- **Estágio:** Atuação no setor de compras do Hospital Unimed Limeira, fortalecendo competências administrativas e organizacionais.
        """
    },
    {
        "titulo": "Educação",
        "conteudo": """
- **Formação:** Gestão da Tecnologia da Informação.
- **Cursos Complementares:** Treinamentos em Inteligência Artificial, Computação em Nuvem, Desenvolvimento e Segurança.
        """
    },
    {
        "titulo": "Habilidades",
        "conteudo": """
- Suporte Técnico e Manutenção de Sistemas (Windows e Linux)
- Segurança de Endpoints e Gerenciamento de Riscos
- Análise de Dados e Melhoria Contínua
- Inteligência Artificial, Computação em Nuvem e Inovação
        """
    },
    {
        "titulo": "Projetos",
        "conteudo": """
- **Github:** [Perfil no Github](https://github.com/trickveiraoficial)
        """
    },
    {
        "titulo": "Certificações",
        "conteudo": """
- Lean Six Sigma Yellow Belt
- Participação em treinamentos especializados em suporte técnico e segurança da informação.
        """
    },
    {
        "titulo": "Informações de Contato",
        "conteudo": """
- **LinkedIn:** [Perfil no LinkedIn](https://www.linkedin.com/in/ids-oliveira/)
- **Email:** trickveira@hotmail.com

        """
    },
]

# Exibição das seções em duas linhas de três colunas cada
col1, col2, col3 = st.columns(3)
with col1:
    with st.expander(secoes[0]["titulo"]):
        st.write(secoes[0]["conteudo"])
with col2:
    with st.expander(secoes[1]["titulo"]):
        st.write(secoes[1]["conteudo"])
with col3:
    with st.expander(secoes[2]["titulo"]):
        st.write(secoes[2]["conteudo"])

col4, col5, col6 = st.columns(3)
with col4:
    with st.expander(secoes[3]["titulo"]):
        st.write(secoes[3]["conteudo"])
with col5:
    with st.expander(secoes[4]["titulo"]):
        st.write(secoes[4]["conteudo"])
with col6:
    with st.expander(secoes[5]["titulo"]):
        st.write(secoes[5]["conteudo"])

# Botão para download do currículo em PDF
try:
    with open("resumo_suporte_2025.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Download do Currículo (PDF)",
        data=PDFbyte,
        file_name="resumo_suporte_2025.pdf",
        mime="application/pdf",
    )
except Exception as e:
    st.error("Arquivo PDF não encontrado.")

# Agradecimento e chamada para contato
st.markdown("""
### Obrigado por visitar!
Entre em contato para saber como posso contribuir para o seu time.
""")
