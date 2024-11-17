import ollama

res = ollama.chat(
	model="llava:13b",
	messages=[
		{
			'role': 'user',
			'content': 'Explain why the answer is C',
			'images': [r"D:\python_projects\teachmegcse\images\sorted\A-level\physics\p1\1\A_phy_p1_646.jpg"]
		}
	]
)

print(res['message']['content'])
