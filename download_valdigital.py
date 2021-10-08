from src.val.valdigital import get_polling_data
import os

sink = os.path.dirname(os.path.abspath(__file__))

get_polling_data(data_sink=sink)
