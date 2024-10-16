from inspect import getmembers, isfunction
import pywhatkit
    
functions_list = getmembers(pywhatkit, isfunction)
print(functions_list[1])
