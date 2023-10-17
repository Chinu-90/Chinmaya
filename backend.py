import openai
from ratelimit import limits, sleep_and_retry
class Chatbot:
    def __init__(self):
        openai.api_key="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"
    def get_response(self,user_input):
        response=openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response
if __name__=="__main__":
    chatbot=Chatbot()
    response=chatbot.get_response("greet me")
    print(response)