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
```python
python client.py -t 0x2b7704221388000577455f8d5f6c8a165e79930949421661481a3c9bb29a4cbe # get and print transaction info
python client.py -t 0x2b7704221388000577455f8d5f6c8a165e79930949421661481a3c9bb29a4cbe -q # get transaction info and make QR code
```