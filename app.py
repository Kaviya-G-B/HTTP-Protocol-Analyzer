from flask import Flask, jsonify, render_template, request
import logging
app = Flask(__name__)
captured_packets = []
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/packets", methods=["GET"])
def get_packets():
    return jsonify(captured_packets)
@app.route("/capture", methods=["POST"])
def capture_packet():
    packet_info = {
        "src_ip": request.remote_addr,
        "dst_ip": "127.0.0.1", 
        "headers": dict(request.headers),
        "body": request.get_data(as_text=True)
    }
    logging.info(f"Captured packet: {packet_info}")
    captured_packets.append(packet_info)
    return "Packet Captured", 200
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8080, debug=True)
