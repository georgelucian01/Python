import time

def main(): 

    my_time = int(input("Enter the time in minutes: "))

    my_time = my_time * 60

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = x // 60 % 60
        hours = x // 3600
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
        

    
if __name__ == "__main__":
    main()