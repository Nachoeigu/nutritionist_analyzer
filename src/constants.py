IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

PROMPT_IMG_RECOGNIZER = "Extract ingredients/nutritional info from the input. Avoid introduction, go beyond the desired output. If is unclear or not visible, answer only 'None'. Otherwise, uniquely list ingedients and/or nutritional info"

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
