def celsius_to_fahrenheit(celsius):
    """将摄氏度转换为华氏度"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """将华氏度转换为摄氏度"""
    return (fahrenheit - 32) * 5/9

# 测试
if __name__ == "__main__":
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"32°F = {fahrenheit_to_celsius(32)}°C")
