from django.shortcuts import render, redirect
import json
from Note.forms import Upload_Form
import markdown
# Create your views here.

htmlcontent = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Reset some default styling */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Full height, background styling */
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            color: #333;
        }

        /* Main container styling */
        .container {
            background: #ffffff;
            padding: 20px 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            width: 90%;
        }

        /* Header styling */
        h1 {
            color: #2c3e50;
            margin-bottom: 16px;
            font-size: 2em;
        }

        /* Paragraph styling */
        p {
            line-height: 1.6;
            font-size: 1.1em;
            color: #555;
            margin-bottom: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
                """


def add_file(request):
    form = Upload_Form()
    message = None
    file_name = "No file"
    if request.method == "POST":
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            print("VAlid")
            message = True
            file = form.cleaned_data['file']
            file_name = str(file).split(".")[0]
            content = str(file.read(), encoding="utf-8")
            tempHTML = markdown.markdown(content)
            with open(f"template/Storage/{file_name}.html", "w", encoding="utf-8") as f2:
                f2.write(htmlcontent)
                f2.write(tempHTML)
                f2.write("""</div>
</body>
</html>""")
            with open("Note_Making/FileNames/files.json", "r+") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
                if data == []:
                    id = 1
                else:
                    id = data[-1]["id"] + 1
                for i in data:
                    if i["Filename"] != file_name:
                        data.append(
                            {"id": id, "Filename": file_name, "Content": content})
                    else:
                        break
                else:
                    data.append(
                            {"id": id, "Filename": file_name, "Content": content})
                f.seek(0)
                json.dump(data, f)
                f.truncate()
        else:
            message = False
        print(file_name)
    return render(request, "index.html", {"form": form, "message": message, "file_name": file_name})


def result(request, file_name):
    return render(request, f"Storage/{file_name}.html")


def savedfile(request):
    with open("Note_Making/FileNames/files.json", "r") as f:
        data = json.load(f)
    return render(request, "saved.html", {"saveddata": data})


def grammarCheck(request, file_name):
    with open("Note_Making/FileNames/files.json", "r") as f:
        data = json.load(f)
        print(data)

        # if form.is_valid():
        #     file = form.cleaned_data['file']
        #     print(file)
    # def check_grammar(note):
    #     # Check for grammar mistakes
    #     matches = tool.check(note)

    #     # Format the response
    #     errors = [
    #         {
    #             "message": match.message,
    #             "replacements": match.replacements,
    #             "offset": match.offset,
    #             "error": match.context
    #         }
    #         for match in matches
    #     ]

    #     return {"errors": errors, "total_errors": len(errors)}

    # # Text to check for grammar issues
    # text = "She were going to the market yesterday to bought some vegetables. Her friend told that they should go by car, but she doesn’t wanted to listen. They buys the vegetables but lefts her wallet at home. So, they decides to return back later. They enjoys the journey despite problem."
    # response = check_grammar(text)
    # offsets = [error['offset'] for error in response['errors']]
    # replacments = [error['replacements'] for error in response['errors']]
    # error_keywords = text.split(" ")
    # length = 0
    # res = ""
    # for i in error_keywords:
    #     if length in offsets:
    #         index = offsets.index(length)
    #         res += f"[{i}] {tuple(replacments[index])} "
    #     else:
    #         res += i + " "
    #     length += len(i) + 1
    #     print(res)
    return render(request, "grammar.html", {"content": data})
