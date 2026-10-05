# Analisador e Gerador de Senhas

Projeto básico em Python com interface gráfica. Ele analisa a senha enquanto
você digita, informa o nível de força, mostra o que falta e cria uma sugestão
mais segura. Também possui uma aba separada para gerar senhas personalizadas e
uma interface escura confortável para uso no computador.

## Recursos

- Análise automática a cada caractere digitado;
- interface totalmente escura;
- barra de força com cores diferentes para cada nível;
- níveis: muito fraca, fraca, intermediária, forte e muito forte;
- lista do que falta para melhorar a senha;
- sugestão automática de senha forte;
- gerador com tamanho de 6 a 128 caracteres;
- opções de maiúsculas, minúsculas, números e caracteres especiais;
- opção para evitar caracteres ambíguos, como `I`, `l`, `1`, `O`, `0` e `o`;
- botão para copiar a senha;
- testes automáticos da lógica.

## O que você pratica neste projeto

- strings e listas;
- funções;
- condições e repetição;
- expressões regulares com `re`;
- geração segura de valores com `secrets`;
- interface gráfica com `tkinter`;
- testes com `unittest`.

> O projeto usa `secrets` em vez de `random`, pois `secrets` é mais apropriado
> para gerar senhas imprevisíveis.

## Como executar no VS Code

1. Instale o Python 3 pelo site oficial e marque a opção **Add Python to PATH**.
2. Extraia a pasta do projeto.
3. Abra a pasta `analisador_senhas` no VS Code.
4. Abra o terminal do VS Code pelo menu **Terminal > Novo Terminal**.
5. Execute:

```bash
python app.py
```

No Windows, se `python` não funcionar, tente:

```bash
py app.py
```

Não é necessário executar `pip install`, pois o projeto usa somente bibliotecas
incluídas no Python.

## Como executar os testes

Dentro da pasta do projeto, execute:

```bash
python -m unittest -v
```

Ou, no Windows:

```bash
py -m unittest -v
```

Se todos os testes exibirem `ok`, a lógica principal está funcionando.

## Estrutura

```text
analisador_senhas/
├── app.py                 
├── password_tools.py      
├── test_password_tools.py  
├── requirements.txt        
├── .gitignore             
