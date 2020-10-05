def search4vowels(phrase):
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))

