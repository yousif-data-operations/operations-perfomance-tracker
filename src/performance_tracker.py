import pygetwindow as gw
import time
import pandas as pd
from datetime import datetime

import sqlite3
class PerformanceTracker:

    def __init__(self, interval_seconds=10):
        self.interval = interval_seconds
        self.data = []

    def track(self, duration_minutes):
        end_time = time.time() + (duration_minutes * 60)

        while time.time() < end_time:
            try:
                window = gw.getActiveWindow()
                if window:
                    self.data.append({
                        "timestamp": datetime.now(),
                        "application": window.title
                    })

                time.sleep(self.interval)

            except Exception:
                continue

        return pd.DataFrame(self.data)

    def export_to_csv(self, filename="performance_log.csv"):
        df = pd.DataFrame(self.data)
        conn =
        sqlite3.connect("performance.db")
        df.to_sql("activity_log",conn,if_exists="append",index=false)
        ()conn.close
        print("performance data saved to sqlite database(performance.db)")
        print(f"Performance log saved to {filename}")


if __name__ == "__main__":
    tracker = PerformanceTracker(interval_seconds=10)
    tracker.track(duration_minutes=1)
    tracker.export_to_csv()
