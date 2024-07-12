import json
import jsonpickle

def serializa_dto(obj):
   #return json.loads(
   #     json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
   #)
    return jsonpickle.encode(obj, unpicklable=False)

