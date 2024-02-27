import random

# Initialize an empty dictionary to store function completion status
functionStatus = {}

def FunctionExample():
    try:
        # Your function code here
        print("Executing FunctionExample")
        
        # Simulate some work being done in the function
        # Randomly choose between 42 and 52 as the result
        result = random.choice([42, 52, 23])
        
        # Mark the function as completed successfully only if the result is 42
        functionStatus['FunctionExample'] = (result == 42)
    
    except:
        # Mark the function as failed if an exception occurs
        functionStatus['FunctionExample'] = False
    
    return result

# Call the example function

def functionLogging():
    while True:
        # Print the function status dictionary after calling the function
        print("Function Status:", functionStatus)

        # Check if all functions were successful
        if all(status for status in functionStatus.values()):
            print("Success")
            break
        else:
            # Ask the user if they want to run the code again
            runAgain = input("Some functions failed. Do you want to run the code again? (yes/no): ")
            runAgain = runAgain.lower()
            if runAgain in ("yes","y"):
                # Reset functionStatus for the next run
                result = FunctionExample()
                # Call
            else:
                print("Exiting.")
                exit()

result = FunctionExample()
functionLogging()