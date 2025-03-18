import os
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class MCPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/search?query="):
            query = self.path.split("query=")[-1]
            # Изменено: начинаем поиск с текущего рабочего каталога, а не с корневого
            response = find_files(os.getcwd(), query)

            # Записываем JSON-ответ в файл
            with open("search_results.json", "w", encoding="utf-8") as json_file:
                json.dump(response, json_file, indent=2, ensure_ascii=False)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def find_files(root_dir, query):
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if query in file:
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                matches.append({
                    "name": file,
                    "path": file_path,
                    "size": file_stat.st_size,
                    "created": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat.st_ctime))
                })
    return matches

def run_server():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MCPRequestHandler)
    print("MCP Server running on port 8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
