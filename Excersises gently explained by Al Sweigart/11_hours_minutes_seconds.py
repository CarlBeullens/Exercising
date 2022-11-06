
def get_hours_minutes_seconds(total_seconds: int) -> str:
    if total_seconds == 0:
        return "0s"
    
    if total_seconds < 60:
        return f"{total_seconds}s"
    
    if 60 <= total_seconds < 3600:
        seconds = total_seconds % 60
        minutes = (total_seconds - seconds) // 60
              
        if minutes and seconds:
            return f"{minutes}m {seconds}s"
        elif minutes:
            return f"{minutes}m"
        elif seconds:
            return f"{seconds}s"
        
    if total_seconds >= 3600:
        seconds = total_seconds % 3600 % 60
        minutes = (total_seconds - seconds) // 60 % 60
        hours = total_seconds // 3600
        
        if hours and minutes and seconds:
            return f"{hours}h {minutes}m {seconds}s"
        elif hours and minutes:
            return f"{hours}h {minutes}m"
        elif hours and seconds:
            return f"{hours}h {seconds}s"
        elif hours:
            return f"{hours}h"
         
            
assert get_hours_minutes_seconds(30) == "30s"
assert get_hours_minutes_seconds(60) == "1m"
assert get_hours_minutes_seconds(90) == "1m 30s"
assert get_hours_minutes_seconds(3600) == "1h"
assert get_hours_minutes_seconds(3601) == "1h 1s"
assert get_hours_minutes_seconds(3661) == "1h 1m 1s"
assert get_hours_minutes_seconds(90042) == "25h 42s"
assert get_hours_minutes_seconds(0) == "0s"