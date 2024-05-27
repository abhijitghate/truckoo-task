import json
from flask import Flask, request,jsonify
from get_displaystring import get_displaystring_for_context
from  resolve_displaystring import resolve_displaystring

app = Flask(__name__)

@app.route("/<displaystringholder>/<locale>/<context>",  methods=["GET"])
def get_displaystring(displaystringholder, locale, context):
  return jsonify({
    "result": get_displaystring_for_context(displaystringholder, locale, context)}), 200

@app.route("/resolve/displaystring",  methods=["POST"])
def resolvedisplaystring():
  data = json.loads(request.data)
  response = resolve_displaystring(data["dictionary"], data["locale"], data["context"])
  return jsonify(response), 200

if __name__ == "__main__":
  app.run(debug=True)
