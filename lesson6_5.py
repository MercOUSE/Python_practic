# Пример 32
def function():
    global var
    var = "new variable"
    print(var)
    
var = "global variable"
function()
print(var)