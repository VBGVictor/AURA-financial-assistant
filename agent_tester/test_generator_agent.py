import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

try:
    # Carregar as variáveis de ambiente do arquivo .env
    print("Carregando variáveis de ambiente...")
    load_dotenv()
    print("Variáveis carregadas.")

    # Inicializar o modelo de linguagem (LLM) do Google Gemini
    print("Inicializando o LLM do Google Gemini...")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-lastest")
    print("LLM inicializado com sucesso!") # <-- NOVO: Confirmação de que o LLM foi criado

    # Criar o template do prompt.
    prompt_template = """
    Você é um engenheiro de software especialista em testes de qualidade (QA).
    Sua tarefa é criar testes unitários em Python usando a biblioteca pytest para o código fornecido.

    **Instruções:**
    1.  Importe a biblioteca pytest.
    2.  Importe as funções necessárias do módulo alvo.
    3.  Crie casos de teste para cenários de sucesso (caminho feliz).
    4.  Crie casos de teste para cenários de falha ou casos extremos (edge cases), como entradas inválidas ou nulas.
    5.  Use a diretiva `pytest.raises` para testar exceções que o código deve levantar.
    6.  Os nomes das funções de teste devem ser claros, começando com `test_`.
    7.  Não adicione nenhum comentário ou explicação no código de teste gerado, apenas o código Python puro.

    **Código para testar:**
    ```python
    {code_to_test}
    ```

    **Arquivo de teste gerado:**
    """

    # Criar o PromptTemplate a partir do template de string.
    prompt = PromptTemplate(
        input_variables=["code_to_test"],
        template=prompt_template
    )

    # Criar a "Chain" que conecta o prompt e o LLM
    chain = LLMChain(llm=llm, prompt=prompt)
    print("Chain criada com sucesso.") # <-- NOVO: Confirmação

    # Ler o código alvo e executar a chain
    print("Lendo o código a ser testado...")
    target_code_path = "financial_functions.py"
    with open(target_code_path, "r", encoding="utf-8") as f:
        code = f.read()
    print("Código lido. Executando o agente para gerar os testes...")

    # --- BLOCO DE DEPURAÇÃO IMPORTANTE ---
    # Vamos rodar a chain dentro de um try...except para capturar qualquer erro silencioso
    generated_test_code = chain.invoke({"code_to_test": code})
    print("--- RESULTADO DA IA ---")
    print(generated_test_code)
    print("--- FIM DO RESULTADO DA IA ---")
    # --- FIM DO BLOCO DE DEPURAÇÃO ---

    # Salvar o resultado em um arquivo de teste
    if generated_test_code and generated_test_code['text']:
        output_filename = f"test_{target_code_path}"
        print(f"Salvando os testes gerados em {output_filename}...")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(generated_test_code['text'])
        print("Processo concluído com sucesso!")
    else:
        print("ERRO: A IA retornou uma resposta vazia. Verifique sua chave de API ou possíveis filtros de segurança.")

except Exception as e:
    print("\n--- OCORREU UM ERRO INESPERADO ---")
    print(f"Tipo de Erro: {type(e).__name__}")
    print(f"Mensagem: {e}")
    print("---------------------------------")
    print("Verifique se sua GOOGLE_API_KEY no arquivo .env está correta e válida.")