# Generate proto services
```
python -m grpc_tools.protoc -I./txproto --python_out=./txmod-client/ --grpc_python_out=./txmod-client/ ./txproto/ethereum.proto
```

# Install and save client requirements
```
cd txmod-client
pip install -r requirements.txt
pip freeze > requirements.txt
```

# Start client
```
python client.py
```