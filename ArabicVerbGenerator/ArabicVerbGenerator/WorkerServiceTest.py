import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import logging

class WorkerService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ArabicVerbGenerator'
    _svc_display_name_ = 'ArabicVerbGenerator.Service'
    _svc_description_ = 'This service runs the ArabicVerbGenerator Python application.'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True
        #self.setup_logging()

    # def setup_logging(self):
    #     logging.basicConfig(filename='C:\\path\\to\\your\\service.log', 
    #                         level=logging.DEBUG,
    #                         format='%(asctime)s - %(levelname)s - %(message)s')

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.new_method()
        self.running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                               servicemanager.PYS_SERVICE_STARTED,
                               (self._svc_name_, ''))
        self.main()

    def main(self):
        # 1 hr
        execution_interval = 60 * 60 
        
        while self.running:
            logging.info("Service is running...")
            time.sleep(execution_interval)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(WorkerService)