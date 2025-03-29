import hashlib
import dadesServer
from dadesServer import User, Child, Tap
from flask import Flask, jsonify, request

token = hashlib.sha256(b"User_id").hexdigest()
print(token)
