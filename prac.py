import PyPDF2


def read_pdf(file_path: str) -> list[str]:
    with open(file_path, "rb") as file:  # The 'b' in 'rb' stands for binary mode
        reader: PyPDF2.PdfReader = PyPDF2.PdfReader(file)
        text_content: list[str] = [page.extract_text() for page in reader.pages]
        return text_content


pages: list[str] = read_pdf("./mypdf.pdf")
print(pages)
