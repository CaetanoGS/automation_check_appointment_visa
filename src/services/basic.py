from datetime import datetime

def time_running_script(start_time) -> str:
    elapsed_time = datetime.now() - start_time
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"Script has been running for: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"