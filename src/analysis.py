
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_survival_results(df):
    plt.figure(figsize=(10, 6))
    for stato in df['Stato_Tessuto'].unique():
        subset = df[df['Stato_Tessuto'] == stato]
        plt.hist(subset['Sopravvivenza'], bins=30, alpha=0.5, label=f'Stato: {stato}')
    plt.title('Distribuzione Sopravvivenza ARES v4.0')
    plt.xlabel('Probabilità di Sopravvivenza')
    plt.ylabel('Frequenza (Pazienti)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('data/processed/survival_plot.png')
    plt.show()
