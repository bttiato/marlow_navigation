import logging

class Logger:
    def __init__(self, logger_name):
        self.log_type = 0
        self.logger_name = logger_name
    
    def setup_logger(self, log_file, log_type=0, log_level=logging.INFO):
        format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        format_date = '%d-%m-%Y %H:%M-%S'
        formatter = logging.Formatter(format_str, datefmt=format_date)
        lib_logger = logging.getLogger(self.logger_name)
        
        if log_type == 0:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            stream_handler.setLevel(log_level)
            lib_logger.addHandler(stream_handler)
        
        else:
            lib_logger.setLevel(log_level)
            file_handler = logging.FileHandler(log_file, mode='w')
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            lib_logger.addHandler(file_handler)
        
        return lib_logger
