import io
from collections import OrderedDict

import xlsxwriter
from django.http import HttpResponse

from calendar import models


def generate_schedule(schedule_id):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Create a workbook.
    workbook = xlsxwriter.Workbook(output)

    # Schedule page.
    schedule_page = workbook.add_worksheet(
        name='Schedule'
    )
    schedule_page.set_header('&CMarina Schedule')
    schedule_page.hide_gridlines(False)
    schedule_page.set_landscape()
    schedule_page.fit_to_pages(1, 0)

    # Name format.
    cell_format_name = workbook.add_format({
        'align': 'left',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': False,
        'text_wrap': False
    })

    # Default format.
    cell_format_default = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': False,
        'text_wrap': True
    })

    # Default col settings.
    schedule_page.set_column(0, 7, 20, cell_format_default)

    # Header format.
    header_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': True,
        'text_wrap': False
    })

    # Set Headers.
    header_names = OrderedDict({
        'A1': [
            'Name',
            header_format
        ],
        'B1': [
            'Sunday',
            header_format
        ],
        'C1': [
            'Monday',
            header_format
        ],
        'D1': [
            'Tuesday',
            header_format
        ],
        'E1': [
            'Wednesday',
            header_format
        ],
        'F1': [
            'Thursday',
            header_format
        ],
        'G1': [
            'Friday',
            header_format
        ],
        'H1': [
            'Saturday',
            header_format
        ]
    })

    for key, value in header_names.items():
        schedule_page.write(key, value[0], value[1])

    schedule = models.Schedule.objects.get(
        pk=schedule_id
    )

    # Schedule name
    schedule_page.write_string(
        row=1,
        col=0,
        string=f"{str(schedule)} \n {str(schedule.time_start)[:-3]} - {str(schedule.time_end)[:-3]}",
        cell_format=cell_format_name.set_text_wrap()
    )

    # Schedule - Sunday
    sunday = [f"{str(item)}" for item in schedule.account_sunday.all()]

    schedule_page.write_string(
        row=1,
        col=1,
        string='\n'.join(map(str, sunday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Monday
    monday = [f"{str(item)}" for item in schedule.account_monday.all()]

    schedule_page.write_string(
        row=1,
        col=2,
        string='\n'.join(map(str, monday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Tuesday
    tuesday = [f"{str(item)}" for item in schedule.account_tuesday.all()]

    schedule_page.write_string(
        row=1,
        col=3,
        string='\n'.join(map(str, tuesday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Wednesday
    wednesday = [f"{str(item)}" for item in schedule.account_wednesday.all()]

    schedule_page.write_string(
        row=1,
        col=4,
        string='\n'.join(map(str, wednesday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Thursday
    thursday = [f"{str(item)}" for item in schedule.account_thursday.all()]

    schedule_page.write_string(
        row=1,
        col=5,
        string='\n'.join(map(str, thursday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Friday
    friday = [f"{str(item)}" for item in schedule.account_friday.all()]

    schedule_page.write_string(
        row=1,
        col=6,
        string='\n'.join(map(str, friday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Schedule - Saturday
    saturday = [f"{str(item)}" for item in schedule.account_saturday.all()]

    schedule_page.write_string(
        row=1,
        col=7,
        string='\n'.join(map(str, saturday)),
        cell_format=cell_format_default.set_text_wrap()
    )

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'Schedule.xlsx'

    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
