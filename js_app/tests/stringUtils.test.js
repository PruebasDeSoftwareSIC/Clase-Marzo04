
// TODO: Escribe pruebas unitarias para isPalindrome.
// Sugerencias: "radar" -> true; "anita lava la tina" -> true; "python" -> false; "" -> true; "Radar" -> true

const { isPalindrome } = require('../src/stringUtils');

test('radar es palindromo', () => {
  expect(isPalindrome('radar')).toBe(true);
});

test('anita lava la tina es palindromo', () => {
  expect(isPalindrome('anita lava la tina')).toBe(true);
});

test('python no es palindromo', () => {
  expect(isPalindrome('python')).toBe(false);
});

test('cadena vacía es palindromo', () => {
  expect(isPalindrome('')).toBe(true);
});

test('Radar es palindromo (ignora mayúsculas)', () => {
  expect(isPalindrome('Radar')).toBe(true);
});