"""Testes automáticos da lógica do projeto."""

import re
import unittest

from password_tools import AMBIGUOUS_CHARACTERS, SPECIAL_CHARACTERS, analyze_password, generate_password


class AnalyzePasswordTests(unittest.TestCase):
    def test_empty_password_is_very_weak(self) -> None:
        result = analyze_password("")
        self.assertEqual(result["level"], "Muito fraca")
        self.assertEqual(result["percentage"], 0)

    def test_common_password_is_detected(self) -> None:
        result = analyze_password("senha123")
        self.assertTrue(result["checks"]["common"])
        self.assertIn("Evite senhas comuns ou fáceis de adivinhar.", result["feedback"])

    def test_balanced_long_password_is_very_strong(self) -> None:
        result = analyze_password("Gato-Azul_92!Rio")
        self.assertEqual(result["level"], "Muito forte")
        self.assertEqual(result["percentage"], 100)
        self.assertEqual(result["feedback"], [])

    def test_repetition_is_detected_with_regex(self) -> None:
        result = analyze_password("Abc!!!123456")
        self.assertTrue(result["checks"]["repetition"])


class GeneratePasswordTests(unittest.TestCase):
    def test_default_password_has_all_character_types(self) -> None:
        password = generate_password(24)
        self.assertEqual(len(password), 24)
        self.assertRegex(password, r"[A-Z]")
        self.assertRegex(password, r"[a-z]")
        self.assertRegex(password, r"\d")
        self.assertTrue(any(character in SPECIAL_CHARACTERS for character in password))

    def test_ambiguous_characters_are_avoided(self) -> None:
        password = generate_password(128, avoid_ambiguous=True)
        self.assertFalse(any(character in AMBIGUOUS_CHARACTERS for character in password))

    def test_only_digits(self) -> None:
        password = generate_password(
            20,
            use_upper=False,
            use_lower=False,
            use_digits=True,
            use_special=False,
        )
        self.assertTrue(re.fullmatch(r"\d{20}", password))

    def test_invalid_length_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(5)
        with self.assertRaises(ValueError):
            generate_password(129)

    def test_no_selected_group_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(
                12,
                use_upper=False,
                use_lower=False,
                use_digits=False,
                use_special=False,
            )


if __name__ == "__main__":
    unittest.main()
