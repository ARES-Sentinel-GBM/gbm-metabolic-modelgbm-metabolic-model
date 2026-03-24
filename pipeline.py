
from src.loader import load_all_raw_models
from src.engine import AresEngine
from src.analysis import plot_survival_results
import pandas as pd
import numpy as np

def run_pipeline():
    print("🚀 Avvio Pipeline Scientifica ARES v4.0...")
    engine = AresEngine()
    
    # Simulazione su scala (N=1.4M come richiesto)
    n = 1400000
    data = {
        'Score_VQE': np.random.uniform(0, 1.8, n),
        'Genetica': np.random.choice(['IDH1-Mut', 'Wild-Type'], n),
        'Condizione': np.random.choice(['Standard', 'MOF'], n)
    }
    df = pd.DataFrame(data)
    
    print("🧠 Esecuzione Diagnostica...")
    df['Stato_Tessuto'] = df['Score_VQE'].apply(engine.classify)
    
    print("💊 Applicazione Protocolli Terapeutici...")
    df['Sopravvivenza'] = df.apply(engine.calculate_survival, axis=1)
    
    print("📊 Generazione Report...")
    plot_survival_results(df)
    df.to_csv('data/processed/final_results.csv', index=False)
    print("✅ Pipeline completata. Risultati in data/processed/")

if __name__ == "__main__":
    run_pipeline()
