import os
from openai import OpenAI
import time

class Nutritionist:

    def __init__(self):
        self.client = OpenAI(api_key = os.getenv('openai_token'))
        
    def new_chat(self, input_text):
        self.thread = self.client.beta.threads.create()

        self.client.beta.threads.messages.create(
        thread_id = self.thread.id,
        role = "user",
        content = f"{input_text}"
        )
            
        run = self.client.beta.threads.runs.create(
        thread_id = self.thread.id,
        assistant_id = 'asst_oEXHXSW0bP7D2gPz39nDxVtd'
        )
        while True:
            run = self.client.beta.threads.runs.retrieve(
            thread_id = self.thread.id,
            run_id = run.id
            )
            
            if run.status == 'completed':
                break

            time.sleep(2)


        messages = self.client.beta.threads.messages.list(
            thread_id = self.thread.id
        )
        print(run)
        result = messages.data[0].content[0].text.value

        return result
