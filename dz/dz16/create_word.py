from docx import Document

def main():
    print("Введите текст для Word-документа:")
    user_text = input("> ")

    doc = Document()
    doc.add_paragraph(user_text)
    
    file_name = "output.docx"
    doc.save(file_name)
    print(f"Файл '{file_name}' успешно создан!")

if __name__ == "__main__":
    main()
