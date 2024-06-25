from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with the actual hash of your public_script.py
KNOWN_HASH = "known_hash_value"  # Update this with your actual hash value
DECRYPTION_KEY = "your_encryption_key"  # Update this with your actual key

# Endpoint to verify the integrity of the client's script
@app.route('/verify-integrity', methods=['POST'])
def verify_integrity():
    script_hash = request.form.get("hash")
    if script_hash == KNOWN_HASH:
        return jsonify({"verified": True}), 200
    return jsonify({"verified": False}), 400

# Endpoint to request the decryption key (can add more complex logic for approval)
@app.route('/request-key', methods=['GET'])
def request_key():
    # In a real-world scenario, you might want to add more checks here
    return jsonify({"key": DECRYPTION_KEY}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
