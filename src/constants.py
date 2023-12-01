IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

PROMPT_IMG_RECOGNIZER = "Extract ingredients/nutritional info. Avoid introduction, go beyond the desired output. If is unclear or not visible, answer only 'None'. Otherwise, list desired info"

HEADERS_IMG_RECOGNIZER_STRUCTURE = {
    "Content-Type": "application/json",
    "Authorization": ""
    }

PAYLOAD_IMG_RECOGNIZER_STRUCTURE = {
    "model": "",
    "messages": [
        {
        "role": "system",
        "content": f"{PROMPT_IMG_RECOGNIZER}"
        },
        {
        "role": "user",
        "content": []
        }
    ],
    "max_tokens": 200
}
