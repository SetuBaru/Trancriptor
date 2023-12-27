from datetime import datetime


# Error Log Handling Mechanism
def LogError(Error='Something Weird is going on'):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    Error_MSG = f"{str(current_time)} : [{str(Error)}]."
    print(f"{Error_MSG}\n")
    try:
        with open(f"_cache_/ERROR_LOGS.txt", "w") as file:
            file.write(f"{Error_MSG}\n")
    except Exception as LoggingError:
        print(f'Encountered {LoggingError} While Handling ErrorLogs.\n')


if __name__ == "__main__":
    LogError()
