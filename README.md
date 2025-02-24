
🧠 IShine - Análise de Sentimentos sobre Saúde Mental
📌 Visão Geral
O IShine é um projeto que utiliza Inteligência Artificial e Processamento de Linguagem Natural (PNL) para analisar sentimentos em postagens sobre saúde mental em redes sociais. O objetivo é identificar padrões emocionais e avaliar como temas como ansiedade, depressão e bem-estar são considerados online.

🚀 Tecnologias Utilizadas
Python (Pandas, NumPy, Scikit-Learn, NLTK)
Aprendizado de Máquina (Naive Bayes, TF-IDF, Redes Neurais)
PNL (Processamento de Linguagem Natural)
API do Twitter/Tweepy (para coleta de dados)
Streamlit (para visualização interativa)
Matplotlib e Seaborn (para geração de gráficos)


Editar
📂 IShine
│── 📁 src                # Código principal
│── 📁 data               # Arquivos de dados
│── 📁 models             # Modelos treinados
│── 📁 notebooks          # Notebooks Jupyter
│── 📄 README.md          # Explicação do projeto
│── 📄 requirements.txt   # Bibliotecas necessárias
│── 📄 .gitignore         # Arquivos ignorados pelo Git

📊 Objetivo do Projeto
O projeto visa responder perguntas como:

Como as pessoas expressam seus sentimentos sobre saúde mental online?
Quais são os padrões mais comuns nos textos desenvolvidos?
Como a inteligência artificial pode ajudar na análise de discursos sobre saúde mental?

🔍 Metodologia
1️⃣ Coleta de Dados – Extração de tweets e postagens sobre saúde mental.
2️⃣ Pré-processamento – Limpeza e tokenização dos textos.
3️⃣ Treinamento do Modelo – Treinamento de um modelo de Machine Learning para classificar sentimentos.
4️⃣ Análise de Resultados – Visualização de padrões através de gráficos.
5️⃣ Dashboard Interativo – Criação de um painel no Streamlit para exploração dos dados.

📥 Como usar o projeto?

1️⃣ Clonar o Repositório

git clone https://github.com/seu-usuario/IShine.git
cd IShine

2️⃣ Instalar como Dependências

pip install -r requirements.txt

3️⃣ Executar uma Coleta de Dados

python src/collect_data.py

4️⃣ Treinar o Modelo

python src/train_model.py

5️⃣ Rodar o Dashboard Interativo

streamlit run src/dashboard.py

📌 Melhorias Futuras
🔄 Treinar modelo mais avançado com BERT ou Transformers.
📊 Crie painel sonoro no Power BI para análise visual mais rica.
📈 Testar Deep Learning (LSTMs) para melhorar a classificação de sentimentos.


📄 Licença
Este projeto está licenciado sob a Licença MIT – sinta-se à vontade para contribuir! 🤝

📬 Contato
📧 E-mail: contato.marypedreira@gmail.com

Se gostou do projeto, deixe um ⭐ no repositório e contribua com melhorias! Obrigada. 🚀

