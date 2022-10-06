import zipfile
import PyPDF2
from io import BytesIO
import pandas as pd


def test_reader():
    name = "resources"

    with zipfile.ZipFile(f'resources/{name}.zip', 'r') as zip_file:
        for file in zip_file.namelist():

            if file.split('.')[-1] == 'pdf':
                pdf_reader = PyPDF2.PdfReader(BytesIO(zip_file.read(file)))
                assert len(pdf_reader.pages) == 1
                for page in pdf_reader.pages:
                    print(page.extract_text())

            elif file.split('.')[-1] == 'csv':
                csv_str = zip_file.read(file).decode("utf-8")
                csv_clean = [r.split(",") for r in [r for r in csv_str.split("\n")]]
                assert len(csv_clean[0]) == 12

            elif file.split('.')[-1] == 'xlsx':
                with zip_file.open(file) as xlsx_file:
                    df = pd.read_excel(xlsx_file)
                    assert len(df.columns) == 6
                    assert 'a' in df.columns
                    assert 'e' in df.columns




test_reader()
