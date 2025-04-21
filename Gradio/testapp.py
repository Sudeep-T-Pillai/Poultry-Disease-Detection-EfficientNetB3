import gradio as gr

# Dummy functions to simulate image processing
def analyze_pose(image):
    return "Pose analysis triggered."

def analyze_fecal(image):
    return "Fecal analysis triggered."

def route_image(choice, image):
    if choice == "Pose":
        return analyze_pose(image)
    elif choice == "Fecal":
        return analyze_fecal(image)
    else:
        return "Please select an analysis type."

with gr.Blocks(css="""
    body { background: linear-gradient(to bottom right, #f7a48b, #fbd774); }
    #title { font-size: 40px; font-weight: bold; text-align: center; margin-top: 3rem; }
    .upload-btn { margin-top: 1.5rem; text-align: center; }
""") as demo:
    gr.Markdown("<div id='title'>Bio Flock</div>")
    
    with gr.Column(elem_classes=["upload-btn"]):
        dropdown = gr.Dropdown(choices=["Pose", "Fecal"], label="Choose analysis type", value="Pose")
        image_input = gr.Image(type="filepath", label="Upload image", interactive=True)
        submit_btn = gr.Button("Click to upload")
        output = gr.Textbox(label="Output")

    submit_btn.click(fn=route_image, inputs=[dropdown, image_input], outputs=output)

demo.launch()
