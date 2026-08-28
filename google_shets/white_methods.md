# gspread 6.x — методы записи

## Запись значений

### `update(values, range_name, ...)`

Основной метод. **В 6.x сначала данные, потом диапазон** (в 5.x было наоборот).

```python
worksheet.update([["a", "b"], ["c", "d"]], "A1:B2")
worksheet.update([["x"]], "C5")        # одна ячейка
worksheet.update([["a", "b"]])         # с A1 по умолчанию
```

По умолчанию `RAW`. Для формул и дат:

```python
from gspread.utils import ValueInputOption

worksheet.update(rows, "A2", value_input_option=ValueInputOption.user_entered)
```

### `update_cell(row, col, value)`

Одна ячейка по числовым координатам (1-based). Всегда `USER_ENTERED`.

```python
worksheet.update_cell(3, 2, "hello")   # B3
```

### `update_acell(label, value)`

То же, но по A1-нотации.

```python
worksheet.update_acell("B3", "hello")
```

### `update_cells(cell_list, ...)`

Читаешь диапазон → правишь `.value` → пишешь пачкой.

**`range()` возвращает плоский список `Cell`, а не двумерный.**
`A1:C7` — это прямоугольник 3x7, но на выходе 21 объект подряд.
Двумерность хранится в атрибутах `cell.row` / `cell.col`, поэтому
перебор идёт по ячейкам, а не по строкам:

```python
cells = worksheet.range("A1:C7")   # len(cells) == 21

for cell in cells:
    if cell.col == 2:              # только столбец B
        cell.value = "x"

worksheet.update_cells(cells, value_input_option=ValueInputOption.user_entered)
```

Если нужна именно двумерная структура — это `get_all_values()`,
который отдаёт `list[list[str]]`.

Диапазон вычисляется как прямоугольник min→max по координатам ячеек.
Для несмежных ячеек в запрос уйдёт всё поле между ними.

### `batch_update(data)`

Несколько несмежных диапазонов за один запрос.

```python
worksheet.batch_update([
    {"range": "A1:B1", "values": [["x", "y"]]},
    {"range": "D5",    "values": [["z"]]},
])
```

## Добавление строк

### `append_row` / `append_rows`

В конец таблицы (ищет первую пустую строку).

```python
worksheet.append_row(["2026-08-28", 121783, "Ivan"])
worksheet.append_rows([row1, row2, row3])          # предпочтительнее
```

### `insert_row` / `insert_rows`

Вставка со сдвигом вниз.

```python
worksheet.insert_row(["header"], index=1)
worksheet.insert_rows([row1, row2], row=5)
```

## Очистка и удаление

```python
worksheet.clear()                          # значения (форматы остаются)
worksheet.batch_clear(["A1:B10", "D1:D5"])
worksheet.delete_rows(2, 10)               # строки 2-10 со сдвигом
worksheet.delete_columns(3)
```

## Квоты

Лимит ~60 запросов в минуту на пользователя. Не писать в цикле:

```python
# плохо — N запросов
for row in rows:
    worksheet.append_row(row)

# хорошо — 1 запрос
worksheet.append_rows(rows)
```

Типовое «стереть и перезалить»:

```python
worksheet.clear()
worksheet.update([header, *rows], "A1", value_input_option=ValueInputOption.user_entered)
```

## Сводка

| Метод | Объём | Адресация | Ввод по умолчанию |
|---|---|---|---|
| `update` | диапазон | A1 | `RAW` |
| `update_cell` | 1 ячейка | `(row, col)` | `USER_ENTERED` |
| `update_acell` | 1 ячейка | A1 | `USER_ENTERED` |
| `update_cells` | список `Cell` | из координат | `RAW` |
| `batch_update` | много диапазонов | A1 | `RAW` |
| `append_rows` | в конец | — | `RAW` |
| `insert_rows` | в конец | — | `RAW` |
