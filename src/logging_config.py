import logging


log_format = "%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s"
log_formater = logging.Formatter(log_format, style="%")

developing_handler = logging.StreamHandler()
developing_handler.setFormatter(log_formater)

product_handler = logging.FileHandler("product_handler.log")
product_handler.setFormatter(log_formater)

