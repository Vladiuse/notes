
### LogRecord default attrs:
<pre> 
%(name)s            # имя логгера
%(levelname)s       # INFO, DEBUG, ERROR ...
%(levelno)s         # числовой уровень (20, 30 ...)
%(pathname)s        # полный путь к файлу
%(filename)s        # имя файла
%(module)s          # имя модуля
%(lineno)d          # номер строки
%(funcName)s        # имя функции
%(created)f         # timestamp (float)
%(asctime)s         # форматированное время (если используется)
%(msecs)d           # миллисекунды
%(relativeCreated)d # время с момента запуска logging
%(thread)d          # id потока
%(threadName)s      # имя потока
%(process)d         # id процесса
%(processName)s     # имя процесса
%(message)s         # итоговое сообщение (msg % args)
</pre>

<pre>
FORMAT = "%(a)s %(b)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.info("logs: %s", "x", extra={"a": "A", "b": "B"})

>> A B logs: x
</pre>
