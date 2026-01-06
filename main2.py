# api.py
from flask import Flask, request, jsonify
from agent import initialize_security_agent
import threading

app = Flask(__name__)

# Initialize the agent ONCE when the app starts
# This prevents reloading the LLM models on every single request
print("⏳ Initializing Security Agent...")
manager_agent = initialize_security_agent()
print("✅ Agent is ready!")

@app.route('/health', methods=['GET'])
def health_check():
    """Simple endpoint to check if API is running"""
    return jsonify({"status": "online", "service": "Security Agent API"})

@app.route('/audit', methods=['POST'])
def run_audit():
    """
    Main endpoint.
    Expects JSON input: { "query": "Check password '12345'" }
    """
    data = request.json
    user_query = data.get('query')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Run the agent (Manager)
        response = manager_agent.run(user_query)
        return jsonify({
            "status": "success",
            "result": response
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)