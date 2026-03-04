import { describe, it, expect } from 'vitest'
import { isPalindrome } from '../src/stringUtils'

// TODO: completa los casos: "radar"->true, "anita lava la tina"->true, "python"->false, ""->true, "Radar"->true

describe('test isPalindrome es true', () => {
  it('radar es palindromo', () => {
    expect(isPalindrome('radar')).toBe(true)
  });
  it('anita lava la tina es palindromo', () => {
    expect(isPalindrome('anita lava la tina')).toBe(true)
  });
  it('cadena vacía es palindromo', () => {
    expect(isPalindrome('')).toBe(true)
  });
  it('Radar es palindromo (ignora mayúsculas)', () => {
    expect(isPalindrome('Radar')).toBe(true)
  });
});

describe('test isPalindrome es false', () => {
  it('python no es palindromo', () => {
    expect(isPalindrome('python')).toBe(false)
  });
});