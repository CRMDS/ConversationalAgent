
import openai
import gradio as gr
import os

openai.api_key = "YOUR API KEY"

query = "What is the capital city of Australia?"
response = openai.Completion.create(
	engine="text-davinci-002",
	prompt=query,
	temperature= 0.1,
	max_tokens = 256,
	top_p = 1,
	best_of = 2,
	frequency_penalty = 0.4,
	presence_penalty=0.3
	)
print(response['choices'][0]['text'])

def greet(query):
	response = openai.Completion.create(
		engine="text-davinci-002",
		prompt=query,
		temperature= 0.1,
		max_tokens = 256,
		top_p = 1,
		best_of = 2,
		frequency_penalty = 0.4,
		presence_penalty=0.3
		)
	answer = response['choices'][0]['text']
	return answer

iface = gr.Interface(fn=greet, inputs="text", outputs="text").launch()
iface.launch()