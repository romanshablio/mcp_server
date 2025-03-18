 # README.md
 readme_content = """
 MCP File Finder Server

## Установка и запуск

 1. Склонируйте репозиторий:
    ```sh
    git clone <ваш-репозиторий>
    cd <ваш-репозиторий>
    ```

# 2. Запустите MCP-сервер:
    ```sh
    python mcp_server.py --port 8080
    ```

# 3. Настройте Cline в VSCode:
    - Откройте `cline_config.json`
    - Скопируйте содержимое в конфигурацию Cline
    - Перезапустите Cline

 ## Тестирование

 Отправьте GET-запрос для поиска файлов:
 ```sh
 curl "http://localhost:8080/search?query=example"
 ```

 Вы получите JSON-ответ с найденными файлами.

 """