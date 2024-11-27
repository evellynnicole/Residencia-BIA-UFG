# Residencia-BIA-UFG
Repositório oficial para o projeto desenvolvido durante o último período do curso de Bacharelado em Inteligência Artificial da Universidade Federal de Goiás (UFG), conhecido como Residência em IA.

# Sobre o Projeto
### Chatbot Conversacional sobre o Campeonato Brasileiro Série A

Este projeto tem como objetivo desenvolver um chatbot conversacional focado em fornecer informações detalhadas sobre o Campeonato Brasileiro Série A. O chatbot foi projetado para ser uma ferramenta prática e intuitiva, permitindo que os usuários obtenham respostas rápidas e precisas sobre temas relacionados ao campeonato, incluindo:

- Partidas: informações sobre jogos anteriores e próximos confrontos.
- Placar e Estatísticas: resultados, número de gols e destaques.
- Horários e Localizações: data, hora e estádio das partidas.
- Detalhes do Jogo: escalações, gols, substituições e cartões.
- Artilharia e Classificação: ranking dos artilheiros e tabela do campeonato.

# Tecnologias Utilizadas
O projeto utiliza técnicas modernas de Inteligência Artificial para oferecer uma experiência conversacional baseada em dados reais do campeonato.

- Text-to-SQL com RAG (Retrieval-Augmented Generation):
  Foi utilizado RAG para recuperar informações como documentação, exemplos de consultas SQL e esquemas de banco de dados. A partir desses dados, o modelo é capaz de construir consultas SQL que respondem às perguntas do usuário, desde que a informação esteja armazenada no banco de dados.

- Tecnologias empregadas:

    - Qdrant: Banco de dados vetorial para armazenamento e recuperação eficiente de embeddings.
    - LangChain: Framework para a integração de modelos e ferramentas de IA.
    - OpenAI: Modelos avançados de linguagem para geração de consultas SQL e respostas.
    - SQLite: Banco de dados para armazenamento estruturado das informações do campeonato.



