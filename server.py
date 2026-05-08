import subprocess
import os
import sys

def run_server():
    # Paths to the internal backend scripts
    ai_dir = os.path.join(os.getcwd(), "SOLAR-DRONE", "Assets", "AI")
    main_server = os.path.join(ai_dir, "main.py")
    emergency_server = os.path.join(ai_dir, "emergency_server.py")

    print("--- Environmental Drone Ecosystem: Server Boot ---")
    
    # 1. Start Main Backend (FastAPI)
    print(f"Launching Main Backend: {main_server}")
    main_process = subprocess.Popen([sys.executable, main_server])

    # 2. Start Emergency Recovery Server (Flask)
    print(f"Launching Emergency Server: {emergency_server}")
    emergency_process = subprocess.Popen([sys.executable, emergency_server])

    try:
        print("\nAll servers active. Use CTRL+C to stop.")
        main_process.wait()
        emergency_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        main_process.terminate()
        emergency_process.terminate()

if __name__ == "__main__":
    run_server()
