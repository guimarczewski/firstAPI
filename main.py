from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"Olá": "Mundo"}

produtos = [{
    "id": 1,
    "nome": "Iphone14",
    "descricao": "Celular da Apple",
    "preco": 5000.00
},{
    "id": 2,
    "nome": "PS4",
    "descricao": "Videogame Sony",
    "preco": 2000.00
},{
    "id": 3,
    "nome": "Workshop do Jupyter pro Deploy",
    "descricao": "Curso",
    "preco": 120.00    
}
]

@app.get("/produtos")
def retorna_a_lista_de_produtos():
    return produtos