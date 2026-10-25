import time
import random
from datetime import datetime
import pandas as pd
from sklearn.ensemble import IsolationForest

class OperationalAIEngine:
    def __init__(self):
        # Initialize an Isolation Forest model to detect operational inefficiencies (anomalies)
        self.anomaly_detector = IsolationForest(contamination=0.1, random_state=42)
        self._bootstrap_model()

    def _bootstrap_model(self):
        """Simulate baseline historical data to train the initial detector."""
        baseline_data = [[random.uniform(50, 70), random.uniform(200, 250)] for _ in range(100)]
        self.anomaly_detector.fit(baseline_data)

    def fetch_sensor_telemetry(self) -> dict:
        """Simulates real-time sensor streams from factory equipment."""
        return {
            "timestamp": datetime.now().isoformat(),
            "energy_consumption_kwh": round(random.uniform(45, 95), 2),  # Spikes simulate high carbon footprint
            "steam_pressure_psi": round(random.uniform(190, 260), 2),
            "carbon_emission_gco2": round(random.uniform(300, 600), 2)
        }

    def process_stream(self):
        print("🚀 Starting Operational AI Carbon Tracking Dashboard...")
        print("Press Ctrl+C to stop.\n")
        
        try:
            while True:
                metrics = self.fetch_sensor_telemetry()
                
                # Reshape data for the ML model
                features = [[metrics["energy_consumption_kwh"], metrics["steam_pressure_psi"]]]
                prediction = self.anomaly_detector.predict(features)
                
                # Interpret isolation forest result (-1 is an anomaly/leakage/inefficiency)
                status = "🟢 OPTIMAL EFFICIENCY"
                action_required = "None"
                
                if prediction[0] == -1 or metrics["energy_consumption_kwh"] > 80:
                    status = "🔴 ANOMALY DETECTED (RESOURCE LEAKAGE)"
                    action_required = "Triggering predictive maintenance alert to prevent carbon spike."

                print(f"[{metrics['timestamp']}]")
                print(f"   Energy: {metrics['energy_consumption_kwh']} kWh | Emissions: {metrics['carbon_emission_gco2']} gCO2")
                print(f"   Status: {status}")
                print(f"   Action: {action_required}")
                print("-" * 60)
                
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nShutting down Operational AI Engine.")

if __name__ == "__main__":
    engine = OperationalAIEngine()
    engine.process_stream()
