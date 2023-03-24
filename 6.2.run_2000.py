
import time


def timer(f, *args, **kwargs):
    # Get the current time
    start_time = time.time()
    # Call the function that was received as a param
    f(*args, **kwargs)
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    return elapsed_time


print("Elapsed time: {:.2f} seconds".format(timer(print, "Hello")))
print("Elapsed time: {:.2f} seconds".format(timer(zip, [1, 2, 3], [4, 5, 6])))
print("Elapsed time: {:.2f} seconds".format(timer("Hi {name}".format, name="Bug")))



