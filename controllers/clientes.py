from app import app
from flask import render_template, request, jsonify


@app.route("/clientes")
def viewClientes():
    return render_template("index.html")


@app.route("/api/clientes", methods=("GET", "POST"))
def clientes():
    try:
        tipoRequisicao = request.method
        if tipoRequisicao == "GET":
            valorNaUrl = dict(request.args)

            if valorNaUrl["tipo"].lower() == "get":
                return valorNaUrl
            
            elif valorNaUrl["tipo"].lower() == "delete":
                return valorNaUrl
            
            else:
                return jsonify({"resposta": "sem acao na rota"})

        
        elif tipoRequisicao == "POST":
            data = request.json
            
            if data["tipo"].lower() == "post":
                return data
            
            elif data["tipo"].lower() == "put":
                return data
            
            else:
                return jsonify({"resposta": "sem acao na rota"})

    except Exception as e:
        return jsonify({"reposta": "algo errado ocorreu", "erro": e})#, 500
