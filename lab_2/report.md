##  Отчет по лаборатоной работе №2

## Результат выполнения первой части задания:

Сгенерированы бинарные псевдослучайные последовательности длиной 128 бит с помощью стандартных ГПСЧ языков C++ и Java

## Результат выполнения второй части задания:

Написана программа на языке Python, реализующая три теста линейки NIST, а также проверены с их помощью сгенерированные последовательности

## Результаты тестов NIST:

# C++:
1) Частотный побитовый тест: P = 0.37675911781158206
2) Тест на одинаковые подряд идущие биты: P = 0.9446095789203891
3) Тест на самую длинную последовательность единиц в блоке: P = 0.4462188631421427

# Java:
1) Частотный побитовый тест: P = 0.4795001221869535
2) Тест на одинаковые подряд идущие биты: P = 0.9646114798766142
3) Тест на самую длинную последовательность единиц в блоке: P = 0.26745460619217515

## Вывод

Обе последовательности, сгенерированные с помошью стандартных ГПСЧ языков C++ и Java, признаются случайными