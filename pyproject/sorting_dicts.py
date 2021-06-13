gods = [
    {"name":"Ares" , "skill":"war"},
    {"name":"Zeus" , "skill":"thunder"},
    {"name":"Hapheastos" , "skill":"iron"}
]

def f(gods):
    return gods["name"]
    
gods.sort(key=f)

print(gods)