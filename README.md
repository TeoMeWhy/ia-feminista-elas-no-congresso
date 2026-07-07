# QuitérIA - A IA Feminista do Elas no Congresso

> **Análise feminista do Legislativo: uma IA open-source para classificar projetos de lei sobre gênero e direitos das mulheres.**

PARTICIPANTE: GIULIA LOBO

## fluxo de trabalho Git local
1. git checkout -b <nova branch> 
2. cria ou atualiza arquivos 
3. git status
---

## 📌 Sumário

- [👁 Visão Geral](#-visão-geral)
- [⚙️ Como Funciona](#-como-funciona)
- [🔄 Dependência de Coleta de Dados](#-dependência-de-coleta-de-dados)
- [📊 Dados de Treinamento](#-dados-de-treinamento)
- [🧪 Etapas do Projeto](#-etapas-do-projeto)
- [📂 Modelo](#-modelo)
  - [Modelo de Classificação de Temas](#modelo-de-classificação-de-temas)
  - [Definição dos Temas](#definição-dos-temas)
  - [Avaliação dos Modelos por Tema](#avaliação)
- [Modelo de Avaliação das Posições dos Projetos](#modelo-de-avaliação-das-posições-dos-projetos)
- [📚 Trabalhos Prévios](#-trabalhos-prévios)
- [🎖️ Conheça Maria Quitéria, nossa homenageada](#-conheça-maria-quitéria-nossa-homenageada)
- [🛠 Versões](#-versões)
- [📄 Licença e Contribuições](#-licença-e-contribuições)

---

## 👁 Visão Geral

A **QuitérIA do Elas no Congresso** é um **projeto de inteligência artificial criado para analisar e rotular automaticamente proposições legislativas (PL)**, com foco em gênero e feminismo. A ferramenta classifica os temas e atribui uma nota que indica o quão desfavoráveis são os PLs aos direitos de gênero.

A solução avaliou a performance de diversos modelos de linguagem pré-treinados e ajustados para classificar os projetos. Este repositório concentra as informações sobre a pesquisa e desenvolvimento de soluções para aperfeiçoar o processo de rotulagem de dados das PL por meio de técnicas de PLN (Processamento de Linguagem Natural) e a coleta automatizada de dados no site da Câmara dos Deputados e do Senado Federal.

---

## ⚙️ Como Funciona

Como parte de seu monitoramento legislativo, a equipe do [Instituto AzMina](https://institutoazmina.org.br/) usa o [Bot do Elas no Congresso](https://github.com/institutoazmina/elasnocongressobot) para coletar as proposições de interesse por meio de palavras-chave. Mas até a edição de 2024, as propostas eram revisadas e rotuladas pela equipe e instituições parceiras com dois objetivos:

- **Tema**: definir o tema da proposta a partir do resumo (ementa) do PL, designando uma das categorias definidas pela contratante;
- **Avaliação**: definir se a proposta é favorável ou não ao direito das mulheres, a partir de uma análise da ementa e do inteiro teor do PL.

Devido ao alto número de propostas coletadas, a rotulagem completamente manual é custosa e demanda alto investimento de recursos humanos. Modelos de inteligência artificial supervisionados poderiam facilitar o processo de rotulagem inicial dos dados.

Assim, a QuitérIA surge com o objetivo de **facilitar a análise e o acompanhamento de projetos de lei** relacionados a temas de gênero, fornecendo **insights automatizados** que auxiliem na tomada de decisão, defesa de políticas públicas e divulgação de informações relevantes.

Implementada em 2025, a classificação automática apresentada aqui **passa por validação humana**, com apoio das mesmas organizações parceiras que já colaboravam no processo anterior. A diferença é que agora as equipes ganham mais tempo para atuar politicamente e produzir conteúdo no site do [Elas no Congresso](https://elasnocongresso.com.br).

---

## 🔄 Dependência de Coleta de Dados

Os dados utilizados para treinar e alimentar os modelos da QuitérIA são coletados automaticamente pelo robô do projeto [Elas no Congresso Bot](https://github.com/institutoazmina/elasnocongressobot).

Este scraper busca proposições legislativas nos sites da Câmara e do Senado, usando palavras-chave relacionadas a gênero, mulheres, direitos feministas e comunidades LGBTQIAP+. As informações extraídas (como título, autor, ementa, status etc.) são salvas em arquivos CSV e posteriormente utilizadas no treinamento e classificação dos modelos de IA.

O código-fonte do robô de coleta está disponível em:  
🔗 https://github.com/institutoazmina/elasnocongressobot

---

## 📊 Dados de Treinamento

Os dados utilizados para o treinamento dos modelos consistem em **resumos de proposições legislativas** em tramitação no Congresso Nacional. Esses dados foram **pré-processados e rotulados manualmente** durante quatro anos e meio, servindo de base para o fine-tuning dos classificadores.

Os dados rotulados estão disponíveis no Hugging Face: [`azmina/ementas_congresso`](https://huggingface.co/datasets/azmina/ementas_congresso)

---

## 🧪 Etapas do Projeto

1. **Pré-processamento de dados**: scripts de limpeza e preparação das proposições legislativas;
2. **Fine-tuning**: ajuste fino dos modelos com base nos dados rotulados manualmente;
3. **Avaliação**: desempenho dos modelos medido por métricas como:
   - Acurácia
   - F1-Score
   - Precisão
   - Recall

---

## 📂 Modelo

### Modelo de Classificação de Temas

Os temas utilizados para classificação dos projetos de lei são:

```
{0: 'economia',
 1: 'genero',
 2: 'dignidade sexual',
 3: 'violencia contra a mulher',
 4: 'politica',
 5: 'direitos sexuais e reprodutivos',
 6: 'direitos sociais',
 7: 'maternidade',
 8: 'feminicidio'}
```

### Definição dos temas:

- **economia**: todas as proposições que envolvem questões de produção, distribuição, acumulação e consumo de bens materiais com recorte de gênero. A categoria inclui, por exemplo, a concessão de benefícios financeiros exclusivos para mulheres e pessoas LGBT, participação econômica de mulheres e outros grupos, abordando temas como igualdade salarial, empreendedorismo feminino, inclusão no mercado de trabalho, acesso a crédito e medidas para combater a precarização do trabalho feminino.

- **gênero**: construções sociais e culturais atribuídas aos papéis masculinos e femininos na sociedade, que influenciam comportamentos, oportunidades e relações entre os sexos. O conceito de gênero é fundamental para entender desigualdades sociais e promover políticas que visem à equidade. Este conjunto de proposições inclui propostas sobre ideologia de gênero, igualdade de gênero, lgbtfobia, orientação sexual e identidade de gênero, propostas para promover a igualdade e eliminar discriminações e preconceitos baseados no gênero, medidas para garantir direitos e oportunidades iguais para mulheres, homens, pessoas trans e não-binárias em áreas como trabalho, educação, saúde, segurança e participação política.

- **dignidade sexual**: refere-se ao reconhecimento do valor de cada indivíduo em relação à sua sexualidade. Isso implica que todas as pessoas têm o direito de viver sua sexualidade de maneira plena e respeitosa, sem discriminação ou violência. A dignidade sexual garante que as relações interpessoais sejam baseadas no respeito mútuo e no consentimento. Neste conjunto de projetos de lei, estão incluídos nessa categoria todos os textos que envolvem crimes contra a dignidade sexual, incluindo estupro e atos relacionados, violação sexual mediante fraude, assédio sexual, divulgação de cena de sexo ou de pornografia, tráfico de pessoas e ato obsceno.

- **violência contra a mulher**: qualquer ato de violência baseado no gênero que resulte em danos para mulheres. Inclui projetos para prevenir, punir e erradicar a violência contra mulheres em todas as suas formas, incluindo violência física, psicológica, sexual, patrimonial e moral. Envolvem políticas de proteção, atendimento e apoio às vítimas, bem como campanhas educativas e ações para responsabilizar os agressores. Essa categoria inclui todos os tipos de violência contra mulheres, com exceção dos crimes contra a dignidade sexual, que estão agrupados em categoria homônima.

- política: atividade relacionada à governança do Estado nos níveis municipal, estadual e federal, e às relações de poder entre indivíduos ou grupos. Envolve proposições legislativas voltadas à participação política das mulheres e à promoção da equidade de gênero na esfera política. Incluem propostas para aumentar a representatividade feminina em cargos eletivos e de liderança, além de garantir a participação em processos de tomada de decisão e elaboração de políticas públicas.

- **direitos sexuais e reprodutivos**: conjunto de direitos humanos que garantem a todos os indivíduos liberdade e capacidade para decidir sobre sua vida sexual e reprodutiva. Isso inclui o direito à informação, à educação, ao acesso a serviços de saúde reprodutiva, ao aborto, ao planejamento familiar, assistência médica durante a gravidez, parto e pós-parto e ao livre exercício da sexualidade.

- **direitos sociais**: aqueles que garantem condições mínimas de vida digna a todos os indivíduos, incluindo acesso à educação, saúde, trabalho, moradia e seguridade social. Esses direitos visam promover a igualdade e a justiça social, assegurando que todos tenham oportunidades iguais para desenvolver seu potencial humano.

- **maternidade**: é a qualidade ou estado de ser mãe, envolvendo não somente o ato biológico da gestação e do parto, mas também o cuidado, educação e proteção oferecidos à criança. Inclui iniciativas sobre licença-maternidade, salário-maternidade e adoção, proteção no ambiente de trabalho, acesso a creches, políticas de apoio à amamentação e assistência a mães em situação de vulnerabilidade.

- **feminicídio**: assassinato de mulheres motivado por questões de gênero, ou seja, por ela ser do sexo feminino. Inclui projetos para prevenir, combater e punir o feminicídio, como políticas para a prevenção, investigação e julgamento de crimes de feminicídio, bem como medidas de apoio e proteção às vítimas de violência de gênero.


### Avaliação

Para avaliação da linha base (baseline), foram utilizados dois modelos de zero-shot e um modelo Naive-Bayes. Para a avaliação final, foram utilizados diversos modelos baseados na arquitetura Transformer, tanto da família BERT quanto aplicações de modelos generativos.

| Modelo                                 | Precisão | Recall | F1   |
|---------------------------------------|-----------|--------|------|
| Naive-Bayes                           | 0.54      | 0.16   | 0.16 |
| [mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) (zero-shot)| 0.32      | 0.28   | 0.27 |
| [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) (zero-shot)  | 0.34      | 0.25   | 0.25 |
| [legal-bert-base-cased-ptbr](https://huggingface.co/dominguesm/legal-bert-base-cased-ptbr)                             | 0.75      | 0.63   | 0.66 |
| [DeBERTina](tgsc/debertina-base-32k-vocab) | 0.82 | 0.74   | 0.75 |
| [BERTimbau large](https://huggingface.co/neuralmind/bert-large-portuguese-cased/)                             | 0.82      | 0.74   | 0.75 |
| [Gemma-9b](https://huggingface.co/unsloth/gemma-2-9b-bnb-4bit)                                 | 0.70      | 0.70   | 0.69 |
| [LLama3-8b](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit)                                | 0.66      | 0.61   | 0.61 |
| [**Congretimbau**](https://huggingface.co/belisards/congretimbau)                          | **0.80**      | **0.79**   | **0.79** |

Melhor desempenho: **Congretimbau**, com F1-score de 0.79  


O modelo com melhor desempenho foi adotado em produção e atingiu as seguintes métricas no conjunto de teste:

|                               | Precision | Recall | F1-Score | Support |
|-------------------------------|-----------|--------|----------|---------|
| Dignidade Sexual              | 0.94      | 0.88   | 0.91     | 17      |
| Direitos Sexuais e Reprodutivos| 0.89      | 0.84   | 0.86     | 19      |
| Direitos Sociais              | 0.61      | 0.58   | 0.59     | 19      |
| Economia                      | 0.78      | 0.50   | 0.61     | 14      |
| Feminicidio                   | 0.67      | 0.80   | 0.73     | 5       |
| Genero                        | 0.81      | 1.00   | 0.90     | 13      |
| Maternidade                   | 0.70      | 0.74   | 0.72     | 19      |
| Politica                      | 1.00      | 0.88   | 0.93     | 8       |
| Violencia Contra a Mulher     | 0.86      | 0.93   | 0.89     | 54      |
| **Accuracy**                  |           |        | 0.82     | 168     |
| **Macro Avg**                 | 0.81      | 0.79   | 0.79     | 168     |
| **Weighted Avg**              | 0.82      | 0.82   | 0.81     | 168     |



### Modelo de avaliação das posições dos projetos

O segundo modelo tem como objetivo identificar propostas desfavoráveis aos direitos das mulheres pela perspectiva feminista interseccional, a partir de um conjunto de dados previamente rotulado pela equipe AzMina e organizações parceiras. O modelo foi treinado a fim de otimizar a identificação de projetos da classe positiva (desfavoráveis aos direitos das mulheres)

Este modelo classifica PLs como:

- **Classe 0 (Favorável)**: Promovem direitos das mulheres, igualdade de gênero, garantias legais.
- **Classe 1 (Desfavorável)**: Representam retrocessos, ameaçam políticas públicas ou ampliam desigualdades.

Após ajuste de limiar, o modelo obteve:
- F1-score de 0.88 para Classe 0
- F1-score de 0.64 para Classe 1


### Avaliação

O modelo atingiu as seguintes métricas no [dataset de avaliação](https://huggingface.co/datasets/azmina/ementas_anotadas_inteiroteor):

|               | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Class 0       | 0.94      | 0.53   | 0.67     | 114     |
| Class 1       | 0.35      | 0.88   | 0.50     | 33      |
| Accuracy      |           |        | 0.61     | 147     |
| Macro Avg     | 0.64      | 0.70   | 0.59     | 147     |
| Weighted Avg  | 0.81      | 0.61   | 0.64     | 147     |

Para uma performance mais equilibrada entre as classes, é possível ajustar o limiar da classificação binária, a partir da análise da curva ROC (disponível no [notebook de avaliação](modelos_avaliacao/avaliacao.ipynb)), chegando aos seguintes resultados:

|               | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Class 0       | 0.91      | 0.86   | 0.88     | 114     |
| Class 1       | 0.59      | 0.70   | 0.64     | 33      |
| Accuracy      |           |        | 0.82     | 147     |
| Macro Avg     | 0.75      | 0.78   | 0.76     | 147     |
| Weighted Avg  | 0.84      | 0.82   | 0.83     | 147     |

## 🎖️ Conheça Maria Quitéria, nossa homenageada
Em 1823, Maria Quitéria se vestiu de homem para lutar pela independência do Brasil, uma coragem que desafiou as expectativas de seu tempo. Dois séculos depois, QuitérIA nasce com o mesmo espírito revolucionário, ocupando os espaços digitais de poder para garantir que as leis brasileiras considerem leis sempre o recorte de gênero. 
Como sua inspiradora, que se disfarçou para acessar espaços de poder, QuitérIA penetra no intrincado sistema legislativo brasileiro, decodificando sua linguagem hermética e revelando impactos muitas vezes invisíveis ao debate público. Nossa arma contemporânea para mudar o futuro é a tecnologia, especialmente dados e algoritmos.
Num contexto onde a complexidade legislativa frequentemente funciona como barreira à participação cidadã, QuitérIA traduz, simplifica e empodera, transformando dados em ação.

## 📚 Trabalhos Prévios

A utilização de modelos de IA em documentos oficiais em português ainda é incipiente. Foi possível identificar trabalhos prévios que utilizam técnicas de processamento de linguagem natural (NLP) para textos legais, mas poucos guardam similaridade com as tarefas em questão. Não foi possível localizar nenhum trabalho prévio focado na classificação de textos legais entre favoráveis ou desfavoráveis aos direitos das mulheres, porém alguns trabalhos anteriores já utilizaram técnicas de NLP para classificação de textos legais em temas pré-determinados.

Os trabalhos listados propõem diferentes categorizações em documentos do âmbito jurídico ou legislativo. Apesar da similaridade da tarefa em questão, estes esforços não servem como um benchmark direto para o nosso projeto, uma vez que a taxonomia e os exemplos diferem daqueles usados no presente projeto. Dito isso, o trabalho que mais se aproxima ao nosso em termos comparativos é o [“A classification approach for estimating subjects of bills in the Brazilian Chamber of Deputies”](https://lume.ufrgs.br/handle/10183/267612), onde o autor experimentou classificadores para temas de proposições da Câmara dos Deputados do Brasil, comparando dois modelos BERT adaptados para o português, usando o texto da ementa. Os melhores resultados relatados foram com o modelo BERTimbau, alcançando 78,94% de pontuação F1 ponderada.

| Referência                                                                                                     | Acurácia | F1-score | Recall |
|---------------------------------------------------------------------------------------------------------------|----------|----------|--------|
| [A classification approach for estimating subjects of bills in the Brazilian Chamber of Deputies](https://lume.ufrgs.br/handle/10183/267612)               | 65%      | 73%      | 70%    |
| [ver BERT: Automating Brazilian Case Law Document Multi-label Categorization Using BERT](https://sol.sbc.org.br/index.php/stil/article/view/17803)                         | 38%      | 71%      | 66%    |
| [Classificação de documentos jurídicos utilizando a arquitetura Transformer: uma análise comparativa com algoritmos tradicionais de Machine Learning e ChatGPT](https://ojs.brazilianjournals.com.br/ojs/index.php/BRJD/article/view/60747) | 62%      | 62%      | 62%    |

## 🛠 Versões
- Transformers 4.45.1
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.20.0

## 📄 Licença e Contribuições

Este repositório contém códigos, modelos próprios e integrações com APIs externas para execução de funcionalidades relacionadas à análise automatizada de proposições legislativas.

Isso significa que você pode:
**Compartilhar** — copiar e redistribuir o material em qualquer suporte ou formato.


**Adaptar** — remixar, transformar e criar a partir do material, para qualquer fim, mesmo que comercial.


Desde que:
**Atribuição** — dê o devido crédito, insira um link para a licença e indique se mudanças foram feitas.


**Compartilhar Igual** — se remixar, transformar ou criar a partir do material, deve distribuir suas contribuições sob a mesma licença.

Além disso, esse projeto segue as diretrizes da Responsible AI License (RAIL) para reforçar práticas éticas no desenvolvimento e uso de IA. Consulte RAIL License.
Ao utilizar este repositório, você **concorda em não empregar o código ou modelos para fins ilegais, discriminatórios, violentos ou que violem direitos humanos**.

**Em resumo:**
Código + modelos próprios → **CC BY-SA 4.0 + RAIL**


Modelos externos → **licença do provedor**, não redistribuídos aqui

### Contribua
Correções, melhorias ou ideias são muito bem-vindas!  
Você pode contribuir diretamente pelo GitHub abrindo uma [issue](https://github.com/institutoazmina/ia-feminista-elas-no-congresso/issues) ou enviando um [pull request](https://github.com/institutoazmina/ia-feminista-elas-no-congresso/pulls).


Ou então, fale com a gente: tecnologia@azmina.com.br 

Vamos construir uma tecnologia feminista e transformadora? 💜
