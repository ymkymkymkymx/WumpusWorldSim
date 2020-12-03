import time
import threading

class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.args = args

    def run(self):
        
        self.result = self.func(*self.args)

    def get_result(self):
        
        try:
            return self.result
        except Exception:
            return None

def limit_decor(timeout, granularity):
    def functions(func):
        def run(*args):
            thre_func = MyThread(target=func, args=args)
            thre_func.setDaemon(True)
            thre_func.start()
            sleep_num = int(timeout//granularity)
            for i in range(0, sleep_num):
                infor = thre_func.get_result()
                if infor:
                    return infor
                else:
                    time.sleep(granularity)
            return None
        return run
    return functions
    
@limit_decor(2, 0.02)
def stopper(agent,ob):
    return agent.move(ob.currentstate())

