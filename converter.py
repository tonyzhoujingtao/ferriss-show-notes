def convert_to_full_urls(base_url: str, show_notes: list):
    total_seconds = convert_to_seconds(time=time)
    full_url = f"{base_url}&t={total_seconds}s"
    return full_url


def convert_to_full_url(base_url: str, time: str):
    total_seconds = convert_to_seconds(time=time)
    full_url = f"{base_url}&t={total_seconds}s"
    return full_url


def convert_to_seconds(time: str):
    time_slice = [int(t) for t in time.split(':')]
    if len(time_slice) <= 0:
        hours, minutes, seconds = 0, 0, 0
    elif len(time_slice) == 1:
        hours, minutes, seconds = [0, 0] + time_slice
    elif len(time_slice) == 2:
        hours, minutes, seconds = [0] + time_slice
    elif len(time_slice) >= 3:
        hours, minutes, seconds = time_slice[:3]

    total_seconds = seconds + minutes * 60 + hours * 60 * 60
    return total_seconds
