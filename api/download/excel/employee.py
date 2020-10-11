import io
from collections import OrderedDict

import xlsxwriter
from django.http import HttpResponse

from calendar import models


def generate_employee(account_id):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Create a workbook.
    workbook = xlsxwriter.Workbook(output)

    # Schedule page.
    schedule = workbook.add_worksheet(
        name='Schedule'
    )
    schedule.set_header('&CMarina Schedule')
    schedule.hide_gridlines(False)
    schedule.set_landscape()
    schedule.fit_to_pages(1, 0)

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
    schedule.set_column(0, 7, 20, cell_format_default)

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
        schedule.write(key, value[0], value[1])

    account = models.Account.objects.get(
        pk=account_id
    )

    # Employee name
    schedule.write_string(
        row=1,
        col=0,
        string=str(account),
        cell_format=cell_format_name
    )

    # Schedule - Sunday
    schedule.write_string(
        row=1,
        col=1,
        string=(f"{str(account.sunday['time_start'])[:-3]} - {str(account.sunday['time_end'])[:-3]}"
                if account.schedule_sunday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Monday
    schedule.write_string(
        row=1,
        col=2,
        string=(f"{str(account.monday['time_start'])[:-3]} - {str(account.monday['time_end'])[:-3]}"
                if account.schedule_monday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Tuesday
    schedule.write_string(
        row=1,
        col=3,
        string=(f"{str(account.tuesday['time_start'])[:-3]} - {str(account.tuesday['time_end'])[:-3]}"
                if account.schedule_tuesday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Wednesday
    schedule.write_string(
        row=1,
        col=4,
        string=(f"{str(account.wednesday['time_start'])[:-3]} - {str(account.wednesday['time_end'])[:-3]}"
                if account.schedule_wednesday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Thursday
    schedule.write_string(
        row=1,
        col=5,
        string=(f"{str(account.thursday['time_start'])[:-3]} - {str(account.thursday['time_end'])[:-3]}"
                if account.schedule_thursday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Friday
    schedule.write_string(
        row=1,
        col=6,
        string=(f"{str(account.friday['time_start'])[:-3]} - {str(account.friday['time_end'])[:-3]}"
                if account.schedule_friday else 'X'),
        cell_format=cell_format_default
    )

    # Schedule - Saturday
    schedule.write_string(
        row=1,
        col=7,
        string=(f"{str(account.saturday['time_start'])[:-3]} - {str(account.saturday['time_end'])[:-3]}"
                if account.schedule_saturday else 'X'),
        cell_format=cell_format_default
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
