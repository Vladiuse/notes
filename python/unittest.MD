<pre> 
m = Mock()

class MyService: ...
m = Mock(spec=MyService)       # только методы/атрибуты, существующие в MyService
m = Mock(spec_set=MyService)   # ещё строже — нельзя создавать новые атрибуты
m = Mock(a=1, b=2, c=3)        # создание мока с атрибуками m.a == 1, m.b == 2
m = Mock(side_effect=func)     # func будет вызываться при call у класса
m = Mock(return_value=123)     # m() == 123

🧩 Подмена атрибутов и методов
m.some_method = Mock()
m.some_attr = "value"
 </pre>

### Мок:

<pre>
mock = Mock()

# Мок атрибута
mock = Mock()
mock.attr = 123
assert mock.attr == 123

# Мок метода
mock.method.return_value = 123
assert mock.method() == 123

# Несколько вызовов
mock.method.side_effect = [1,2,3]
assert mock.method() == 1
assert mock.method() == 2
assert mock.method() == 3
mock.method() # raise StopIteration

# вызов ошибки
mock.method.side_effect = ZeroDivisionError("boom")
mock.method() # ZeroDivisionError: boom

# через функцию
def test():
    return "test"

mock.method.side_effect = test
assert mock.method()  == "test"
</pre>

## patch

### @patch

<pre>
class A:
    attr = "A_attr"
    def run(self):
        return "A_run"
# mock method
@patch("__main__.A.run", return_value=123)
def test_1(mock):
    assert A().run() == 123
# mock class
@patch("__main__.A", return_value=123)
def test_2(mock):
    assert A() == 123, f"actual: {A().run()}"

# mock attr
@patch("__main__.A.attr", 123)
def test_3():
    assert A().attr == 123
</pre>

### with patch
<pre> 
class A:
    def run(self):
        return "A_run"
# запокать по пути
with patch("__main__.A.run", return_value=123):
    assert A().run() == 123

# замокать обьект
with patch.object(A, "run", return_value=123):
    assert A().run() == 123

# замокать атрибуты
with patch.multiple(X, a="x", b="x"):
    x = X()
    assert x.a == "x"
    assert x.b == "x"
</pre>


## 📘 Часто используемые атрибуты Mock

| Атрибут / Метод             | Описание                                    |
|-----------------------------|---------------------------------------------|
| `assert_called()`           | Проверки вызовов                            |
| `assert_called_once()`      | Был вызван один раз                         |
| `assert_called_once_with()` | Был вызван один раз с указанными атрибутами |
| `assert_any_call()`         | Хотя бы один вызов с указаными атрибутами   |
| `assert_not_called()`       | Мок не вызывался                            |
| `assert_has_calls()`        | Можно указать какие вызовы должны были быть |
| `reset_mock()`              | Сброс состояния                             |
| `return_value`              | Что возвращать при вызове                   |
| `side_effect`               | Последовательность / функция / исключение   |
| `called`                    | Был ли вызван                               |
| `mock_calls`                | Спписок всех вызовов                        |
| `call_count`                | Количество вызовов                          |
| `call_args`                 | Последние аргументы вызова                  |
| `call_args_list`            | Все вызовы                                  |
| `attach_mock()`             | Вложенные моки                              |
| `configure_mock()`          | Массовая конфигурация атрибутов             |
| `mock_add_spec()`           | Добавить спецификацию постфактум            |


