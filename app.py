from flask import Flask, send_file

app = Flask(__name__)

@app.route('/app.apk')
def serve_apk():
    try:
        return send_file('app.apk', as_attachment=True)
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    # Run on all interfaces so external devices can access
    app.run(host='0.0.0.0', port=8000)
