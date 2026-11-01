import uuid

novo_id = uuid.uuid4()
print(novo_id)
print(type(novo_id))
print(len(str(novo_id)))

import json
print(json.dumps({'ID': str(novo_id)}))