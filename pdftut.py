from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import subprocess


# Creates new decrypted copy
def decrypter(path, id):
    id_dict = {
        1: r"C:\Users\Dvir\Documents\PdfCompile\temp\DecPdf1.pdf",
        2: r"C:\Users\Dvir\Documents\PdfCompile\temp\DecPdf2.pdf",
        3: r"C:\Users\Dvir\Documents\PdfCompile\temp\DecPdf3.pdf",
    }
    new_path = id_dict[id]
    try:
        subprocess.run(["qpdf ", "--decrypt", path, new_path])
        return new_path
    except ValueError:
        print("Oops, looks like the path incorrect.")


def merger(start_chapt, end_chapt, chapters, file1, engfile, engpage, file2):
    pdf_file1 = PdfFileReader(open(file1, "rb"))
    eng_file = PdfFileReader(open(engfile, "rb"))
    pdf_file2 = PdfFileReader(open(file2, "rb"))
    output_file = PdfFileWriter()
    file_length = pdf_file1.getNumPages()
    for i in range(0, start_chapt + 1):
        output_file.addPage(pdf_file1.getPage(i))
        

    for chapter in chapters:
        for j in range(int(chapter['start_page']), int(chapter['end_page']) + 1):
            if chapter['num'] < 6:
                if not (chapter['chap_type'] == 'e1' or chapter['chap_type'] == 'e2'):
                    output_file.addPage(eng_file.getPage(engpage))
                output_file.addPage(pdf_file1.getPage(j))
            else:
                output_file.addPage(eng_file.getPage(engpage))
                output_file.addPage(pdf_file2.getPage(j))

    for i in range(end_chapt, file_length):
        output_file.addPage(pdf_file1.getPage(i))

    output_path = open(r"C:\Users\Dvir\Documents\PdfCompile\newPDF.pdf", "wb")
    output_file.write(output_path)
    output_path.close()


def spliter(path, temp_dict, chap_name):
    file = open(path, 'rb')
    pdf_reader = PdfFileReader(file)
    pdf_writer = PdfFileWriter()
    start_page = int(temp_dict['start_page'])
    end_page = int(temp_dict['end_page'])
    for i in range(start_page, end_page + 1):
        pdf_writer.addPage(pdf_reader.getPage(i))
    temp_path = r'C:\Users\Dvir\Documents\PdfCompile\temp\chap' + chap_name
    split_file = open(temp_path, 'wb')
    pdf_writer.write(split_file)
    split_file.close()
    file.close()
    return temp_path








