import time
import signal
from datetime import datetime

# set to always run unless interrupted
running = True

# handle keyboard interrupt from command prompt/terminal (CTRL + C)
def sig_handler(sig, frame):
    print("Signal Interrupted...")
    global running
    running = False

# register keyboard interrupt
signal.signal(signal.SIGINT, sig_handler)

# path of file i want to create
file_path = r"D:\test.txt"

# create the file
def create_file(file_path):
    # write empty file
    with open(file_path, 'w') as f:
        f.write("")

def read_write_loop(file_path, iterations = 1000, timeout = .15, target_bytes = 100_000, max_duration = 60):
    error_count = 0
    total_tests = 0
    total_written = 0

    start_time = time.time()

    with open(file_path, 'w+') as f:
        while running and total_written <= target_bytes and (time.time() - start_time) <= max_duration:
            for i in range(1, iterations+1):
                # check if keyboard interrupt
                if not running:
                    break
                
                # check to see if it passed the duration
                #if (time.time() - start_time) > max_duration:
                #    break

                if total_written > target_bytes:
                    break
                
                # compile what I want to write
                current_time = datetime.now().strftime("%H:%M:%S")
                write = f"test {i} at {current_time}\n"
                start_write_time = time.time()

                #write to file
                f.seek(0,2) #move to end of file
                f.write(write) #write the line
                f.flush() #ensure its written to disk

                #check amount of time needed to write
                write_time = time.time() - start_write_time
                total_written += len(write)

                if(write_time > timeout):
                    error_count += 1
                    error_rate = error_count/(total_tests+1) * 100 if total_tests > 0 else 100
                    print(f"    FAIL at line {i}. Write took {write_time:.2f}s, more than timeout of {timeout:.2f}s.")
                    print(f"    Error count = {error_count}, Error rate = {error_rate:.2f}% of {total_tests+1} total tests")
                    continue

                print(write.strip()) #print for visibility

                #read from file
                start_read_time = time.time()
                f.seek(f.tell() - (len(write) + 1)) # move to start of line just finished
                read = f.readline()
                read_time = time.time() - start_read_time

                if read_time > timeout:
                    error_count += 1
                    error_rate = error_count/(total_tests+1) * 100 if total_tests > 0 else 100
                    print(f"    FAIL at line {i}. Read took {read_time:.2f}s.")
                    print(f"    Error count = {error_count}, Error rate = {error_rate:.2f}% of {total_tests+1} total tests")
                    continue

                total_tests += 1

                #verify
                if read != write:
                    print(f"    FAIL at line {i}. Wrote '{write.strip()}', read '{read.strip()}'.")
                    error_count += 1
                    error_rate = error_count/total_tests * 100
                    print(f"    Error count = {error_count}, Error rate = {error_rate:.6f}% of {total_tests} total tests")

                # go back to beginning when it reaches the max i
                if i == iterations:
                    print(f"    Starting new {iterations} Tests...")
                    f.seek(0)
                    f.truncate()
                
                time.sleep(0.001)

            #time.sleep(0.10)
    
    # consider how long the test was
    end_time = time.time()
    duration = end_time - start_time
    error_rate_per_byte = error_count / total_written if total_written > 0 else 0
    print("..................................")
    print(f"Total Duration: {duration:.2f} seconds")
    print(f"Total Bytes Written: {total_written}")
    print(f"Error Count: {error_count}")
    print(f"Error Rate Per Byte: {error_rate_per_byte:.6f}%")
    if error_rate_per_byte < 1e-6:
        print("    - Within Limit")
    else:
        print("    - Exceeds Limit")

try:
    create_file(file_path)
    read_write_loop(file_path)
except Exception as e:
    print(f"An error has occured: {e}")