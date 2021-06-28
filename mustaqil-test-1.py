import platform
import datetime
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
print(platform.processor())
print(platform.architecture())
print(platform.machine())
print(platform.system())
print(platform.python_compiler())
print(platform.platform())
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
