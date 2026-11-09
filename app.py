import os
from jwt_info_gen import app, generate_jwt_with_info

if __name__ == "__main__":
    # Pterodactyl ke liye port 4031, warna default 5000
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=False)
