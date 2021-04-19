# Notes: 算出时针的角度和分针的角度，相减得到夹角，比较取最小值即可。
# 注意因为24小时制，所以时针要做换算比如13点换成1点。时针一格是30度，一小时60分钟等于一分钟时针走0.5度。而分针则是固定一分钟6度。
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour >= 12:
            hour = hour - 12
        angleHour = 30*hour + (30/60)*minutes
        angleMinutes = 6*minutes
        return min(abs(angleHour-angleMinutes), 360-abs(angleHour-angleMinutes))