PROMPT_IMG_RECOGNIZER = "Extract ingredients/nutritional info from the provided image. Avoid introduction, go beyond the desired info. Expected output: Ingredients:'...' Nutritional Info: '...'"

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
