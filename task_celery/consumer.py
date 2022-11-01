import time
from tasks import sum

# Task Producer
if __name__ == '__main__':
    for x in range(0,100):
        result = sum.delay(x, 10)
        time.sleep(10)
        print(f"Done {x}")