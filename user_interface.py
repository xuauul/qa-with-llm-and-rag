import gradio
from gradio.themes.base import Base

def create_user_interface(model):
  with gradio.Blocks(theme=Base(), title="Question Answering App using Vector Search + RAG") as app:
    gradio.Markdown(
      """
      # Interactive Question Answering App

      Explore the power of Atlas Vector Search combined with Langchain's RetrieverQA and OpenAI LLM!
      """)

    textbox = gradio.Textbox(label="Enter your question:")

    with gradio.Row():
      button = gradio.Button("Submit", variant="primary")

    with gradio.Column():
      output1 = gradio.Textbox(lines=1, max_lines=10, label="Results with Atlas Vector Search alone:")
      output2 = gradio.Textbox(lines=1, max_lines=10, label="Results with Atlas Vector Search + RetrieverQA + OpenAI LLM:")

    button.click(model.run, textbox, outputs=[output1, output2])

  return app