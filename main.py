# main.py
import threading
import uvicorn
from scheduler import start_scheduler

def run_api():
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000)

def run_scheduler():
    start_scheduler()

if __name__ == "__main__":
    # run both in parallel
    api_thread = threading.Thread(target=run_api)
    scheduler_thread = threading.Thread(target=run_scheduler)

    api_thread.start()
    scheduler_thread.start()

    api_thread.join()
    scheduler_thread.join()