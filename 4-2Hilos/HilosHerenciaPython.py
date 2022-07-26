import threading
import time


class HilosHerenciaPython(threading.Thread):

    
    cont = 0
    bandera = True

    

    def HilosHerenciaPython(self, c):
        self.cont = c
    
    def start(self):
        while self.bandera:
            print(self.cont)
            self.cont+=1
            if self.cont>100:
                self.bandera = False


    
    
def worker():
        print(threading.current_thread().getName(), 'Starting')
        time.sleep(0.2)
        print(threading.current_thread().getName(), 'Exiting')


if __name__ == "__main__":
    HilosHerenciaPython(name='worker', target=worker).start()
    HilosHerenciaPython(name='worker', target=worker).start()