import store

from fastapi import FastAPI


app = FastAPI()

#decorador es lo del arroba osea la linea 9 la 10 ya es parte del codigo
@app.get("/")
def get_list():
    return[1,2,3,]

@app.get("/contact")
def get_list():
    return{'name': "MIRA MARTIN HICE UNA PAGINA WEB CON PYTHON XD"}

def run():
    store.get_categories()
if __name__=='__main__':
    run()