from glob import glob
import re
import os
import win32com.client as win32
from win32com.client import constants


def change_word_format(file_path):
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(file_path)
        doc.Activate()

        # Rename path with .doc
        new_file_abs = os.path.abspath(file_path)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatDocument
        )
        doc.Close(False)
    except Exception as e:
        word.ActiveDocument.Close()


change_word_format("F:\For Study\VNUK\CSZ\Tools\ExamForm\CPM3e_TB_ch02.MultiChoice.rtf")