from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada de modelos de telegramas
telegram_models = {
    "despido": "Por la presente, rechazo el despido comunicado el FECHA, por resultar improcedente. Exijo el pago de indemnizaciones conforme a la legislación vigente. Reservo derechos.",
    "suspension": "Rechazo la suspensión impuesta el FECHA por maliciosa e improcedente. Desconozco los hechos referenciados y responsabilizo a la empresa por los salarios caídos. Reservo derechos."
}

@app.route('/consulta', methods=['POST'])
def consulta():
    data = request.json
    tipo = data.get("tipo")
    fecha = data.get("fecha", "FECHA")
    
    if tipo in telegram_models:
        telegrama = telegram_models[tipo].replace("FECHA", fecha)
        return jsonify({"telegrama": telegrama})
    else:
        return jsonify({"error": "Tipo de telegrama no encontrado"}), 400

@app.route('/actualizar_modelo', methods=['POST'])
def actualizar_modelo():
    data = request.json
    tipo = data.get("tipo")
    nuevo_modelo = data.get("modelo")
    
    if tipo and nuevo_modelo:
        telegram_models[tipo] = nuevo_modelo
        return jsonify({"mensaje": "Modelo actualizado correctamente"})
    else:
        return jsonify({"error": "Datos insuficientes"}), 400

if __name__ == '__main__':
    app.run(debug=True)
