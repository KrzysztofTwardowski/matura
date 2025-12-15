from collections import Counter
from collections.abc import Iterable, Iterator
from functools import cache, partial
from itertools import compress, islice, count
from math import ceil, isqrt


def zadanie31(liczby: Iterable[int]) -> tuple[int, int]:
    kwadraty_całkowitych = [
        liczba for liczba in liczby
        if isqrt(liczba) ** 2 == liczba
    ]
    ilość = len(kwadraty_całkowitych)
    pierwsza = kwadraty_całkowitych[0]
    return ilość, pierwsza


@cache
def liczby_pierwsze(rozmiar=10_000) -> tuple[int, ...]:
    sito = [True] * rozmiar
    sito[:2] = [False] * 2
    for i in range(2, isqrt(rozmiar) + 1):
        if sito[i]:
            ilość = ceil(rozmiar / i) - i
            sito[i * i:: i] = [False] * ilość
    return tuple(compress(count(), sito))


def różne_czynniki(liczba: int) -> Iterator[int]:
    for pierwsza in liczby_pierwsze():
        if liczba % pierwsza == 0:
            yield pierwsza
        if pierwsza >= liczba:
            break


def zadanie32(liczby: Iterable[int]) -> Iterator[int]:
    for liczba in liczby:
        czynniki = islice(różne_czynniki(liczba), 5)
        ilość = sum(1 for _ in czynniki)
        if ilość == 5:
            yield liczba


def procedura(liczba: int) -> int:
    cyfry_rosnąco = ''.join(sorted(str(liczba)))
    cyfry_malejąco = cyfry_rosnąco[::-1]
    return int(cyfry_malejąco) - int(cyfry_rosnąco)


def zadanie33(liczby: Iterable[int]) -> tuple[dict[str, int], list[int]]:
    równe = []
    ilości: dict[str, int] = Counter()
    for liczba in liczby:
        wynik = procedura(liczba)
        if wynik > liczba:
            ilości['większa'] += 1
        elif wynik < liczba:
            ilości['mniejsza'] += 1
        else:
            ilości['równa'] += 1
            równe.append(liczba)
    return ilości, równe


def main():
    with open('liczby.txt') as plik:
        liczby = list(map(int, plik))

    with open('wyniki3.txt', 'w') as plik:
        zapisz = partial(print, file=plik)

        zapisz("Zadanie 3.1:")
        zapisz(*zadanie31(liczby))

        zapisz("\nZadanie 3.2:")
        zapisz(*zadanie32(liczby), sep='\n')

        zapisz("\nZadanie 3.3:")
        zapisz(*zadanie33(liczby), sep='\n')


if __name__ == "__main__":
    main()
