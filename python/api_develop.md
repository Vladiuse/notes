# Подходы к представлению данных в API-клиенте

Вопрос: какие есть подходы к тому, как API-клиент отдаёт данные — от простых до сложных.

## 1. `dict[str, Any]` / сырой JSON

Просто отдаёшь `response.json()` как есть.

```python
from typing import Any


def get_conversion(offer_id: int) -> dict[str, Any]:
    response = requests.get(...)
    return response.json()
```

Плюсы: ноль усилий. Минусы: с mypy strict бесполезно — везде `Any`, нет автодополнения, легко опечататься в ключе и не узнать об этом до рантайма. Годится только для быстрых скриптов/прототипов.

## 2. `TypedDict`

Типизированный словарь — структура есть, но это всё ещё `dict` под капотом.

```python
from typing import TypedDict


class KeitaroConversionDict(TypedDict):
    click_id: str
    status: str


def get_conversion(offer_id: int) -> KeitaroConversionDict:
    response = requests.get(...)
    return response.json()  # type: ignore[no-any-return]
```

Плюсы: mypy проверяет ключи и типы значений при обращении. Минусы: **нет валидации в рантайме** — если API вернёт не то, что описано, ты узнаешь об этом не сразу, а где-то дальше по коду при обращении к несуществующему ключу. Плюс нельзя добавить методы/поведение.

## 3. `NamedTuple`

Неизменяемый, лёгкий, с атрибутами через точку.

```python
from typing import NamedTuple


class KeitaroConversion(NamedTuple):
    click_id: str
    status: str


def get_conversion(offer_id: int) -> KeitaroConversion:
    data = response.json()
    return KeitaroConversion(click_id=data["click_id"], status=data["status"])
```

Плюсы: неизменяемость, распаковка `x, y = conversion`, дешёвый. Минусы: тоже без валидации, для сложных вложенных структур неудобен, нет `.model_dump()`-подобных удобств.

## 4. `dataclass`

Самый популярный средний вариант.

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KeitaroConversion:
    click_id: str
    status: str


def get_conversion(offer_id: int) -> KeitaroConversion:
    data = response.json()
    return KeitaroConversion(click_id=data["click_id"], status=data["status"])
```

Плюсы: читаемо, можно добавлять методы/свойства, `frozen=True` — иммутабельность, `slots=True` — экономия памяти. Минусы: **тоже нет валидации типов в рантайме** — если руками собираешь объект из `data["..."]`, а там придёт `int` вместо `str`, dataclass это не проверит.

## 5. `attrs`

По сути расширенная версия dataclass, была популярна до появления `pydantic v2`/встроенных dataclass-фич. Есть валидаторы, конвертеры.

```python
import attrs


@attrs.define
class KeitaroConversion:
    click_id: str = attrs.field(converter=str)
    status: str
```

На практике сейчас чаще выбирают между обычным `dataclass` и `pydantic`, `attrs` реже — но знать полезно, иногда встречается в чужом коде.

## 6. `pydantic.BaseModel`

Сейчас, по сути, стандарт для API-клиентов в Python-экосистеме.

```python
from pydantic import BaseModel


class KeitaroConversion(BaseModel):
    click_id: str
    status: str


def get_conversion(offer_id: int) -> KeitaroConversion:
    response = requests.get(...)
    response.raise_for_status()
    return KeitaroConversion.model_validate(response.json())
```

Плюсы: **валидация в рантайме из коробки** — если API пришлёт `status: 123` вместо строки — либо приведёт к `str`, либо кинет `ValidationError`, ты сразу узнаешь, что контракт с внешним API нарушен. Есть `model_validate`, `model_dump`, алиасы полей (`Field(alias="clickId")` — удобно, когда в JSON camelCase), вложенные модели, кастомные валидаторы. Минусы: чуть медленнее dataclass, дополнительная зависимость (хотя у тебя она и так в стеке).

Для клиента к нестабильному/недокументированному API (как часто с Keitaro) это обычно лучший баланс — сразу видно, если вендор поменял формат ответа.

## 7. `pydantic.dataclasses.dataclass`

Гибрид — синтаксис как у обычного dataclass, но с pydantic-валидацией под капотом.

```python
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class KeitaroConversion:
    click_id: str
    status: str
```

Полезно, если хочешь оставаться "в парадигме" dataclass (например, для совместимости с другим кодом), но получить валидацию.

## 8. Доменные объекты / rich models (с поведением)

Когда DTO мало и нужна бизнес-логика поверх данных — оборачиваешь в класс с методами, часто поверх pydantic/dataclass.

```python
from pydantic import BaseModel


class KeitaroConversion(BaseModel):
    click_id: str
    status: str

    @property
    def is_approved(self) -> bool:
        return self.status == "lead"
```

Это уже не просто «структура данных», а объект с поведением — уместно, когда клиент используется не только для передачи данных дальше, а логика интерпретации ответа завязана на эти данные.

## 9. ORM-подобные объекты (Active Record)

Редко в API-клиентах, но встречается — объект знает, как сам себя сохранить/обновить через API (`conversion.save()`, `conversion.refresh()`). Обычно так делают SDK крупных вендоров (Stripe SDK, например). Для своего клиента overkill в большинстве случаев — усложняет тестирование и создаёт скрытые side-effects.

---

## Практическая рекомендация

Для клиентов к Keitaro/Affilka/AlanBase — `pydantic.BaseModel`. Pydantic уже в стеке, mypy strict с ним дружит хорошо (особенно v2), и валидация в рантайме критична именно потому, что это внешние недокументированные/полу-документированные API, где легко словить неожиданный формат ответа.