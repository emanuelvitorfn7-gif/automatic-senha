"""Regras de análise e geração de senhas.

Este módulo não cria a interface. Assim, sua lógica pode ser testada de forma
independente e reaproveitada em outros projetos.
"""

import re
import secrets
import string


SPECIAL_CHARACTERS = "!@#$%^&*_-+=?"
AMBIGUOUS_CHARACTERS = "Il1O0o"
COMMON_PASSWORDS = {
    "123456",
    "12345678",
    "123456789",
    "admin",
    "password",
    "qwerty",
    "senha",
    "senha123",
}


def analyze_password(password: str) -> dict:
    """Analisa uma senha e retorna nível, pontuação e recomendações.

    A função utiliza expressões regulares para reconhecer os diferentes tipos
    de caracteres e alguns padrões que enfraquecem uma senha.
    """

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9\s]", password))
    has_repetition = bool(re.search(r"(.)\1\1", password))
    is_common = password.lower() in COMMON_PASSWORDS

    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    score += sum((has_lower, has_upper, has_digit, has_special))

    if password and len(set(password)) / len(password) >= 0.60:
        score += 1
    if password and not has_repetition:
        score += 1
    if password and not is_common:
        score += 1

    score = min(score, 10)

    if score <= 2:
        level = "Muito fraca"
    elif score <= 4:
        level = "Fraca"
    elif score <= 6:
        level = "Intermediária"
    elif score <= 8:
        level = "Forte"
    else:
        level = "Muito forte"

    # Uma senha curta ou com pouca variedade não deve receber nível alto,
    # mesmo que tenha pontuado em outros critérios.
    category_count = sum((has_lower, has_upper, has_digit, has_special))
    if len(password) < 8 and score > 4:
        level = "Fraca"
    elif len(password) < 12 and score > 6:
        level = "Intermediária"
    elif category_count < 3 and score > 6:
        level = "Intermediária"

    percentage_by_level = {
        "Muito fraca": min(score * 10, 20),
        "Fraca": min(max(score * 10, 25), 40),
        "Intermediária": min(max(score * 10, 45), 60),
        "Forte": min(max(score * 10, 70), 80),
        "Muito forte": min(max(score * 10, 90), 100),
    }

    feedback = []
    if len(password) < 12:
        feedback.append("Use pelo menos 12 caracteres (16 ou mais é ainda melhor).")
    if not has_upper:
        feedback.append("Adicione pelo menos uma letra maiúscula.")
    if not has_lower:
        feedback.append("Adicione pelo menos uma letra minúscula.")
    if not has_digit:
        feedback.append("Adicione pelo menos um número.")
    if not has_special:
        feedback.append("Adicione pelo menos um caractere especial, como !, @ ou #.")
    if has_repetition:
        feedback.append("Evite repetir o mesmo caractere três vezes seguidas.")
    if is_common:
        feedback.append("Evite senhas comuns ou fáceis de adivinhar.")

    return {
        "level": level,
        "score": score,
        "percentage": percentage_by_level[level],
        "feedback": feedback,
        "checks": {
            "length_12": len(password) >= 12,
            "lower": has_lower,
            "upper": has_upper,
            "digit": has_digit,
            "special": has_special,
            "repetition": has_repetition,
            "common": is_common,
        },
    }


def generate_password(
    length: int = 18,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
    avoid_ambiguous: bool = True,
) -> str:
    """Gera uma senha segura com as opções selecionadas.

    ``secrets`` é usado no lugar de ``random`` porque foi criado para gerar
    valores imprevisíveis adequados a senhas e tokens.
    """

    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError("A quantidade de caracteres precisa ser um número inteiro.")
    if not 6 <= length <= 128:
        raise ValueError("Escolha uma quantidade entre 6 e 128 caracteres.")

    selected_groups = []
    if use_upper:
        selected_groups.append(string.ascii_uppercase)
    if use_lower:
        selected_groups.append(string.ascii_lowercase)
    if use_digits:
        selected_groups.append(string.digits)
    if use_special:
        selected_groups.append(SPECIAL_CHARACTERS)

    if not selected_groups:
        raise ValueError("Ative pelo menos um tipo de caractere.")

    if avoid_ambiguous:
        selected_groups = [
            "".join(character for character in group if character not in AMBIGUOUS_CHARACTERS)
            for group in selected_groups
        ]

    if length < len(selected_groups):
        raise ValueError("O tamanho escolhido é menor que a quantidade de grupos ativos.")

    # Garante ao menos um caractere de cada grupo selecionado.
    characters = [secrets.choice(group) for group in selected_groups]
    complete_pool = "".join(selected_groups)

    characters.extend(
        secrets.choice(complete_pool) for _ in range(length - len(characters))
    )
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)
