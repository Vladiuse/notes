## Django Cache — основные методы

```python   
from django.core.cache import cache

cache.set("key", "value", timeout=60)          # записать (timeout в секундах, None = бессрочно)
cache.get("key")                               # прочитать, вернёт None если нет/истёк
cache.get("key", "default")                    # с дефолтным значением, если ключа нет
cache.delete("key")                            # удалить ключ
cache.has_key("key")                           # проверить наличие (bool)

cache.add("key", "value", timeout=60)          # записать, только если ключа ещё нет (вернёт False, если уже есть)
cache.get_or_set("key", "value", timeout=60)   # получить, а если нет — сразу записать и вернуть

cache.incr("counter")                          # +1 (ключ должен существовать, иначе ValueError)
cache.incr("counter", 5)                       # +5
cache.decr("counter")                          # -1

cache.set_many({"a": 1, "b": 2}, timeout=60)   # массовая запись
cache.get_many(["a", "b"])                     # массовое чтение -> {"a": 1, "b": 2}
cache.delete_many(["a", "b"])                  # массовое удаление

cache.clear()                                  # очистить весь кэш (текущий backend/alias)

cache.touch("key", timeout=60)                 # обновить TTL без изменения значения
```