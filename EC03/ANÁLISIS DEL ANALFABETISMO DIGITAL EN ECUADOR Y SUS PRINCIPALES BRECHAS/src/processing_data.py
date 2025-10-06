
import pandas as pd
import matplotlib.pyplot as plt
import numpy

from src.cleaning import retornar_dataframe


class Data:
    def __init__(self):
        self.df = retornar_dataframe()

    def show_dataframe(self):
        print(self.df)