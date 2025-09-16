# AURA - Assistente Financeiro Pessoal com IA

# AURA: Assistente Unificado de Risco e Automação para o Setor Financeiro

## Visão Geral do Projeto

AURA é uma plataforma de IA interna projetada para dar suporte a todo o ciclo de vida de desenvolvimento de modelos de Machine Learning no setor financeiro. O objetivo é integrar DevSecOps (Desenvolvimento, Segurança e Operações) em uma única interface inteligente para acelerar a entrega, garantir a qualidade do código e mitigar riscos de segurança.

### Módulos Principais
1.  **Núcleo de MLOps:** Um agente de IA que gera automaticamente testes unitários (`pytest`) para funções Python, garantindo a qualidade e a confiabilidade do código.
2.  **Guardião de Segurança:** Uma API que analisa diagramas de arquitetura de software e gera automaticamente uma análise de ameaças baseada na metodologia STRIDE.
3.  **Interface de Comando:** Um assistente virtual conversacional (voz e texto) que serve como a interface unificada para interagir com todos os módulos da plataforma.

### Arquitetura: 
1. Receber uma pergunta do usuário
2. Coletar dados via API dos Modulos escolhidos
3. Processar e analisar os dados com a biblioteca Pandas
4. Enviar os dados estruturados para uma LLM via API da [gemini-1.5-pro-lastest] com um prompt engenheirado
5. Apresentar a resposta gerada ao usuário.

### Tecnologias: 
Python, LangChain, Pandas, API-gemini-1.5-pro-lastest (até o momento).

## Configuração do Ambiente
*(Esta seção será atualizada à medida que os módulos forem desenvolvidos)*

## Como Usar
*(Esta seção será atualizada à medida que os módulos forem desenvolvidos)*
