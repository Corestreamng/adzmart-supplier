import os
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django import forms

class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])

class XLHEADERS():
    NAME = 'name',
    UNIT_TYPE = 'unit_type',
    SUPPLIER = 'supplier',
    DISPLAY_NAME = 'display_name',
    REFERENCE_ID = 'reference_id',
    BILLBOARD_ID = 'billboard_id',
    LATITUDE = 'latitude',
    LONGITUDE = 'longitude',
    DISTRICT = 'district',
    STATE = 'state',
    POSTAL_CODE = 'postal_code',
    COUNTRY = 'country',
    FACING = 'facing',
    DESCRIPTION = 'description',

    MP_CODE = 'Mp_Code',
    VENDOR_NAME = 'Vendor_Name',
    CORPORATE_NAME = 'Corporate_Name',
    STATION_NAME = 'Station_Name',
    STATE_NAME = 'State',
    MEDIA_TYPE = 'Media_Type',
    RATE_DESC = 'Rate_Desc',
    TIME = 'Time',
    DURATION = 'Duration',
    CARD_RATE = 'Card_Rate',
    NEGO_RATE = 'Nego_Rate',
    CARD_VD = 'Card_VD',
    NEGO_VD = 'Nego_VD',
    CARD_SC = 'Card_SC',
    NEGO_SC = 'Nego_SC',
    Add_VD = 'Add_VD',
    SP_DISC = 'SP_Disc',
    AGENCY = 'Agency',
    VAT = 'VAT',
    MONDAY = 'Mon',
    TUESDAY = 'Tue',
    WEDNESDAY = 'Wed',
    THURSDAY = 'Thu',
    FRIDAY = 'Fri',
    SATURDAY = 'Sat',
    SUNDAY = 'Sun',

    billboard_choices = [NAME, UNIT_TYPE, SUPPLIER, DISPLAY_NAME, REFERENCE_ID, BILLBOARD_ID, LATITUDE, LONGITUDE, DISTRICT, STATE, POSTAL_CODE, COUNTRY, FACING, DESCRIPTION]
    imod_choices = [MP_CODE, VENDOR_NAME, CORPORATE_NAME, STATION_NAME, STATE_NAME, MEDIA_TYPE, RATE_DESC, TIME, DURATION, CARD_RATE, NEGO_RATE, CARD_VD, NEGO_VD, CARD_SC, NEGO_SC, Add_VD, SP_DISC, AGENCY, VAT, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

def get_file_headers(ws, action):
    headers_row = None 
    headers = {}

    # Get headers row
    for row in range(ws.max_row + 1):
        # consider empty rows in worksheet and get the fist instance of the headers
        cell = ws['A'][row].value
        
        # select header choices based on url
        header_choices = None
        if action == 'catalog:upload_billboard_catalog':
            header_choices = list(map(''.join, XLHEADERS.billboard_choices))

        else:
            header_choices = list(map(''.join, XLHEADERS.imod_choices))

        if isinstance(cell, str) and cell in header_choices:
            headers_row = row
            break

    # capture rows with no headers
    if headers_row is None:
        return None, None

    # remember position of headers
    file_header = []
    for i in range(ws.max_column):
        column = chr(i + 65) # go through columns using ASCII('A'-'Z')
        header = ws[column][headers_row].value
        file_header.append(header)
        if header is None:
            break
        
        # check if header is in XLHEADERS billboard
        for choice in XLHEADERS.billboard_choices:
            if header in choice:
                headers[choice] = i
                break

        # check if header is in XLHEADERS imod
        for choice in XLHEADERS.imod_choices:
            if header in choice:
                headers[choice] = i
                break
            
    # capture absent and unkown headers in billboard upload
    absent_cols_billboard = set(XLHEADERS.billboard_choices).difference(headers)
    unknown_cols_billboard = set(file_header).difference(list(map(''.join, headers)))

    # convert list of tuples to list of strings in billboard upload
    absent_cols_conv_billboard = list(map(''.join, absent_cols_billboard))
    unknown_cols_conv_billboard = list(map(''.join, unknown_cols_billboard))

    # capture absent and unkown headers in tv/radio upload
    absent_cols_imod = set(XLHEADERS.imod_choices).difference(headers)
    unknown_cols_imod = set(file_header).difference(list(map(''.join, headers)))

    # convert list of tuples to list of strings in tv/radio upload
    absent_cols_conv_imod = list(map(''.join, absent_cols_imod))
    unknown_cols_conv_imod = list(map(''.join, unknown_cols_imod))
        
    return (headers_row, headers, 
            absent_cols_conv_billboard, 
            unknown_cols_conv_billboard, 
            absent_cols_conv_imod, 
            unknown_cols_conv_imod, 
            )

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file type. Kindly upload an excel file and try again.')

def validate_file_size(value):
    filesize = value.size 
    if filesize > 1048576: # files should not be > 1MB
        raise ValidationError("You cannot upload file more than 1MB. Kindly check the file size and try again.")
    else:
        return value
