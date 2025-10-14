<pre> 
m = Mock()

class MyService: ...
m = Mock(spec=MyService)       # только методы/атрибуты, существующие в MyService
m = Mock(spec_set=MyService)   # ещё строже — нельзя создавать новые атрибуты

🧩 Подмена атрибутов и методов
m.some_method = Mock()
m.some_attr = "value"
 </pre>


### Вызов метода:
<pre> 
m.some_method(1, 2, key="x")
m.some_method.assert_called_once()
m.some_method.assert_called_with(1, 2, key="x")
 </pre>


### Один результат
<pre> 
m.some_method.return_value = 42
print(m.some_method())  # 42
 </pre>


### Разные результаты по вызовам
<pre> 
m.some_method.side_effect = [1, 2, 3]
print(m.some_method())  # 1
print(m.some_method())  # 2
 </pre>


### Возврат значения через функцию
<pre> 
def dynamic_result(arg):
    return arg * 2

m.some_method.side_effect = dynamic_result
print(m.some_method(5))  # 10
 </pre>

### Исключение при вызове
<pre> 
m.some_method.side_effect = ValueError("boom")
m.some_method()  # поднимет ValueError("boom")
 </pre>


## 🧨 Проверка вызовов
<pre> 
m.some_method.called                # bool — был ли вызван
m.some_method.call_count            # количество вызовов
m.some_method.call_args             # последний вызов (args, kwargs)
m.some_method.call_args_list        # список всех вызовов
m.some_method.assert_called()       # просто факт вызова
m.some_method.assert_called_once()  # ровно один раз
m.some_method.assert_called_with(1, 2)
m.some_method.assert_any_call(1, 2)
m.some_method.assert_has_calls([call(1), call(2)])
m.some_method.reset_mock()          # сброс счётчиков и вызовов
 </pre>


## 🧠 Подмена поведения через patch
<pre> 
from unittest.mock import patch

@patch("path.to.module.ClassName")
def test_something(mock_class):
    instance = mock_class.return_value
    instance.do_stuff.return_value = 123
 </pre>
### Контекстный менеджер:

<pre> 
with patch("path.to.module.function_name", return_value=42) as mock_func:
    assert function_name() == 42
 </pre>

### 🔍 Комбинированный пример
<pre> 
from unittest.mock import Mock, call
import pytest

def test_mock_example():
    service = Mock()
    service.fetch.side_effect = [1, 2, ValueError("fail")]

    assert service.fetch() == 1
    assert service.fetch() == 2
    try:
        service.fetch()
    except ValueError:
        pass

    service.fetch.assert_has_calls([call(), call(), call()])
    assert service.fetch.call_count == 3
 </pre>


## 📘 Часто используемые атрибуты Mock
| Атрибут / Метод    | Описание                                        |
| ------------------ | ----------------------------------------------- |
| `return_value`     | Что возвращать при вызове                       |
| `side_effect`      | Последовательность / функция / исключение       |
| `called`           | Был ли вызван                                   |
| `call_count`       | Количество вызовов                              |
| `call_args`        | Последние аргументы вызова                      |
| `call_args_list`   | Все вызовы                                      |
| `assert_called*()` | Проверки вызовов                                |
| `reset_mock()`     | Сброс состояния                                 |
| `spec`, `spec_set` | Ограничивают доступные атрибуты                 |
| `attach_mock()`    | Вложенные моки                                  |
| `configure_mock()` | Массовая конфигурация атрибутов                 |
| `mock_add_spec()`  | Добавить спецификацию постфактум                |
| `wraps`            | Оборачивает реальный объект, сохраняя поведение |

