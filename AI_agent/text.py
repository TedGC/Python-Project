import sys
import os

print("--- DIAGNOSTIC CHECK ---")
print(f"1. Path to Python being used: {sys.executable}")
print(f"2. Current Working Directory: {os.getcwd()}")
print(f"3. Searching for libraries in: {sys.path[:3]}")

try:
    import langchain_core
    print("✅ Success: langchain_core is found!")
except ImportError:
    print("❌ Error: langchain_core is NOT found in this environment.")