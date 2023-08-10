import docx

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs]
        content = '\n'.join(paragraphs)
        print(content)
    except:
        pass

    return content

# Usage example
file_path = 'C:/Users/cricd/Desktop/akash.docx'
content = read_docx(file_path)
print(content)
