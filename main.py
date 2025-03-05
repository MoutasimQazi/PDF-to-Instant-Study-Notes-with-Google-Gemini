import os
import google.generativeai as genai
from openpyxl import Workbook
from google.colab import files  # For easy file download
import markdown
import codecs

# --- Configuration ---
GEMINI_API_KEY = ""  # Replace with your actual API key. Less secure than env var.
OUTPUT_FILE = "gemini_responses_with_structure.xlsx"
GENERATION_CONFIG = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# --- Function to safely handle API calls ---
def get_gemini_response(model, prompt):
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Error processing prompt '{prompt}': {e}")
        return f"Error: {e}"

# --- Main execution ---
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=GENERATION_CONFIG)

    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Input", "Response"])

    for input_text in questions_array:
        detailed_prompt = input_text
        response_text = get_gemini_response(model, detailed_prompt)
        sheet.append([input_text, response_text])

    workbook.save(OUTPUT_FILE)
    print(f"Responses saved to {OUTPUT_FILE}")
    files.download(OUTPUT_FILE)  # Download the file directly

except Exception as e:
    print(f"An error occurred: {e}")


def convert_web_to_html():
    # Read Markdown content
    with codecs.open("set.md", 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html = markdown.markdown(md_content, extensions=['extra', 'toc'])

    # Full HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Software Engineering Questions and Answers</title>
    <style>
        :root {{
            --primary-color: #2D3748;
            --secondary-color: #4FD1C5;
            --tertiary-color: #F7FAFC;
            --highlight-color: #F56565;
            --border-color: #E2E8F0;
        }}
        body {{
            font-family: 'Arial', sans-serif;
            background-color: var(--tertiary-color);
            color: var(--primary-color);
            margin: 0;
            padding: 2rem;
            height: 100vh;
            overflow: auto;
        }}
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--tertiary-color);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
        }}
        .password-box {{
            background-color: #fff;
            border-radius: 8px;
            padding: 40px;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            text-align: center;
            animation: fadeIn 0.5s ease-out;
        }}
        .password-box h2 {{
            margin-bottom: 20px;
            font-size: 1.5rem;
            color: var(--primary-color);
        }}
        .password-box input {{
            padding: 12px;
            margin-bottom: 20px;
            font-size: 1.1rem;
            border: 1px solid var(--border-color);
            border-radius: 5px;
            width: 100%;
            box-sizing: border-box;
            background-color: #f9f9f9;
            color: var(--primary-color);
        }}
        .password-box button {{
            padding: 12px 25px;
            background-color: var(--secondary-color);
            color: #fff;
            font-size: 1.1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s ease;
        }}
        .password-box button:hover {{
            background-color: var(--highlight-color);
        }}
        .content {{
            display: none;
        }}
    </style>
</head>
<body>
    <div class="overlay" id="passwordOverlay">
        <div class="password-box">
            <h2>Enter Password</h2>
            <input type="password" id="passwordInput" placeholder="Password">
            <button onclick="checkPassword()">Submit</button>
        </div>
    </div>
    <div id="mainContent">
        {html}
    </div>
    <script>
        function checkPassword() {{
            var password = document.getElementById("passwordInput").value;
            var correctPassword = "dontstudy";
            if (password === correctPassword) {{
                document.getElementById("passwordOverlay").style.display = "none";
                document.getElementById("mainContent").style.display = "block";
            }} else {{
                alert("Incorrect password. Please try again.");
            }}
        }}
        document.getElementById("passwordInput").addEventListener("keypress", function(event) {{
            if (event.key === "Enter") {{
                event.preventDefault();
                checkPassword();
            }}
        }});
    </script>
</body>
</html>"""

    # Write HTML file
    with codecs.open("software_engineering_answers.html", 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Conversion completed! Check software_engineering_answers.html")

# Run the function
convert_web_to_html()
