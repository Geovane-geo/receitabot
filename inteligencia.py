import google.generativeai as genai

def detectar_ingridientes(chave, imagem):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel("gemini-2.0-flash")
    prompt = ''' Liste quais são os ingredientes dessa imagem.
    Os ingredintes devem ser apresentados em uma lista separada por vírgula, como no exemplo a seguir.
    Nenhum texto adicional deve ser gerado como reposta além dos próprios ingredientes.

    #Exemplo de saída
    Arroz, Feijão, Frango.
    '''


    resposta = modelo.generate_content([prompt, imagem])
    
    ingredientes = resposta.text.split(',')
# O método join() é geralmente mais eficiente do que usar um loop for e concatenar strings manualmente.
    ingredientes_limpos = [ingrediente.strip() for ingrediente in ingredientes] 

# Junta os ingredientes em uma string separada por vírgulas
    ingredientes_formatados = " ,  ".join(ingredientes_limpos)

    return ingredientes_formatados
     

def possiveis_receitas(chave, ingredientes):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f''' Considerando a seguinte lista de ingredientes, gere uma lista de receitas culinárias que os utilizem.
    As receitas devem tentar incluir a maior parte dos ingredientes.
    Gere apenas uma lista com os nomes das receita, separados por Pontos.
    # Lista de Ingredientes
    {ingredientes}
    #Exemplo de saída
        Receita 1, 
        Receita 2,
        Receita 3
    '''
    resposta = modelo.generate_content([prompt])
    receitas = resposta.text.split(".")

    # Remove espaços em branco extras e valores vazios da lista
    receitas_limpas = [receita.strip() for receita in receitas if receita.strip()] #strip é para deixar o texto limpo

    return receitas_limpas

def receita_completa(chave, ingredientes, receita):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f''' Crie a receita para o prato: "{receita}".
    inclua a maior quantidade possivel dos ingredientes da lista de ingredientes.

    # Lista de Ingredientes
    {ingredientes}

    '''
    resposta = modelo.generate_content([prompt])

    return resposta.text