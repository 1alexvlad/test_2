import logging
import copy
import sys 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)

def get_user_id() -> int | None:
    return 123

class UserContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> logging.LogRecord:
        record = copy.copy(record)
        record.user_id = get_user_id()
        return record


stream_handler.addFilter(UserContextFilter())

stream_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s user_id=%(user_id)s: %(message)s",
        defaults={"user_id": "-"},
    )
)
logger.addHandler(stream_handler)

logger.debug("Начинаю создавать заказ")
logger.info("Заказ создан")
logger.warning("API создания заказа недоступен, пытаюсь ещё раз...")
logger.error("API создания заказа совсем недоступен, 3 попытки не помогли")
logger.critical("Ошибка конфигурации системы, выключаюсь")
