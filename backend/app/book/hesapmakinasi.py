from sanic import Sanic
from sanic.response import json

app = Sanic("MySanicApp")

@app.route("/")
async def test(request):
    return json({"message": "Hello, Sanic!"})

@app.route("/calculate", methods=["GET"])
async def calculate(request):
    return toplamaislemi(request)






    # URL parametrelerini alıyoruz
    try:
        param1 = int(request.args.get("ilknumara", 0))  # Varsayılan değer 0
        param2 = int(request.args.get("ikincinumara", 0))
        result = param1 + param2  # Örneğin toplama işlemi
        return json({"result": result})
    except (ValueError, TypeError):
        return json({"error": "Lütfen geçerli sayılar gönderin!"}, status=400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)