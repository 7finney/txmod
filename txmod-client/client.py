#!/usr/bin/python3

# Copyright 2020 mathcody.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC ethereum client."""

from __future__ import print_function
import logging
import json
from termcolor import cprint
import pyqrcode
import subprocess
import sys, getopt

import grpc

import ethereum_pb2
import ethereum_pb2_grpc

def getTxInfo(txHash):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50054') as channel:
        ethstub = ethereum_pb2_grpc.ProtoEthServiceStub(channel)
        request = ethereum_pb2.GetTxReq(networkid=1, txhash=txHash)
        try:
            resp = ethstub.GetTransaction(request)
            tx = json.loads(resp.transaction)
            cprint('Transaction info:', 'yellow',)
            cprint(tx, 'green')
            return tx
        except grpc.RpcError as rpc_error:
            cprint(f'RPC failed with error: {rpc_error}', 'red')
def makeQR(txInfo):
    cprint("generating QR code...")
    txqr = pyqrcode.create(json.dumps(txInfo))
    txqr.png('transaction.png', scale=6)
    cprint('transaction.png created', 'green')
    subprocess.run(["xdg-open", "transaction.png"])

def run():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:vq", ["help", "transaction="])
    except getopt.GetoptError:
      print('client.py -t <input transaction> -q <QR file>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('client.py -t <input transaction> -q <QR file>')
            sys.exit()
        elif opt in ("-t", "--intx"):
            txInfo = getTxInfo(arg)
        elif opt in ("-q", "--qr"):
            makeQR(txInfo)

if __name__ == '__main__':
    logging.basicConfig()
    run()