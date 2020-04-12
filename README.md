# generate proto services
```
python -m grpc_tools.protoc -I./txproto --python_out=./txmod-client/ --grpc_python_out=./txmod-client/ ./txproto/ethereum.proto
```

# install and save client requirements
```
pip install -r requirements.txt
pip freeze > requirements.txt
```