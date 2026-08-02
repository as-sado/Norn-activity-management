import threading
from apscheduler.schedulers.background import BackgroundScheduler
from utils.getCurrenGUI import grafInterface

def check_active_window():
    window = grafInterface.get_initial_class() 
    print(window)

def main():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        check_active_window,
        "interval",
        seconds=1
    )

    scheduler.start()


    try:
        threading.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()



if __name__ == "__main__":
    main()