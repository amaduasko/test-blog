import xlsxwriter
from constants import sheet_header
from build_data.db import db



async def fetch_xml_doc(file_name='users'):
    path = f'data/{file_name}.xlsx'

    # create file if it doesn't exist
    open(path, 'w+')
    workbook = xlsxwriter.Workbook(path)

    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet()

    # add header

    for header in sheet_header:
        worksheet.write(header,sheet_header[header], bold)
    
    # add columns
    data = db.get_users_selections()
    for index, user in enumerate(data):
        worksheet.write_row(f'A{index+2}', [user.fio,f'{user.datar}', user.role])
    
    workbook.close()

    file = open(path, 'rb')

    print('File generated !')

    return file
 