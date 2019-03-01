"""
Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Precondition:
00:00 <= time <= 23:59
"""

def sun_angle(time):
    time_ = float(time.replace(":", "."))
    time_hours = float(time.split(":")[0])
    time_minutes = float(time.split(":")[1])
    angle_per_hour = 180/12
    angle_per_minute = 180/12/60
    if 0 < time_ < 6.0 or 18.0 < time_ < 24.0:
        return "I don't see the sun!"
    angle = (time_hours - 6.00) * angle_per_hour + time_minutes * angle_per_minute
    return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("06:00") == 0
    assert sun_angle("18:00") == 180
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("18:01") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")