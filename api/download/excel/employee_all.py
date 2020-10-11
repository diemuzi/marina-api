import io
from collections import OrderedDict

import xlsxwriter
from django.http import HttpResponse

from calendar import models


def generate_employee_all():
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

    row = 0

    account = models.Account.objects.all()

    dow = {}

    for item in account:
        row += 1

        # Employee name
        schedule.write_string(
            row=row,
            col=0,
            string=str(item),
            cell_format=cell_format_name
        )

        dow.update({
            'sunday': (f"{str(item.sunday['time_start'])[:-3]} - {str(item.sunday['time_end'])[:-3]}"
                       if item.schedule_sunday else 'X'),
            'monday': (f"{str(item.monday['time_start'])[:-3]} - {str(item.monday['time_end'])[:-3]}"
                       if item.schedule_monday else 'X'),
            'tuesday': (f"{str(item.tuesday['time_start'])[:-3]} - {str(item.tuesday['time_end'])[:-3]}"
                        if item.schedule_tuesday else 'X'),
            'wednesday': (f"{str(item.wednesday['time_start'])[:-3]} - {str(item.wednesday['time_end'])[:-3]}"
                          if item.schedule_wednesday else 'X'),
            'thursday': (f"{str(item.thursday['time_start'])[:-3]} - {str(item.thursday['time_end'])[:-3]}"
                         if item.schedule_thursday else 'X'),
            'friday': (f"{str(item.friday['time_start'])[:-3]} - {str(item.friday['time_end'])[:-3]}"
                       if item.schedule_friday else 'X'),
            'saturday': (f"{str(item.saturday['time_start'])[:-3]} - {str(item.saturday['time_end'])[:-3]}"
                         if item.schedule_saturday else 'X')
        })

        # Schedule - Sunday
        schedule.write_string(
            row=row,
            col=1,
            string=dow['sunday'],
            cell_format=cell_format_default
        )

        # Schedule - Monday
        schedule.write_string(
            row=row,
            col=2,
            string=dow['monday'],
            cell_format=cell_format_default
        )

        # Schedule - Tuesday
        schedule.write_string(
            row=row,
            col=3,
            string=dow['tuesday'],
            cell_format=cell_format_default
        )

        # Schedule - Wednesday
        schedule.write_string(
            row=row,
            col=4,
            string=dow['wednesday'],
            cell_format=cell_format_default
        )

        # Schedule - Thursday
        schedule.write_string(
            row=row,
            col=5,
            string=dow['thursday'],
            cell_format=cell_format_default
        )

        # Schedule - Friday
        schedule.write_string(
            row=row,
            col=6,
            string=dow['friday'],
            cell_format=cell_format_default
        )

        # Schedule - Saturday
        schedule.write_string(
            row=row,
            col=7,
            string=dow['saturday'],
            cell_format=cell_format_default
        )

        # Employee page.
        employee_page = workbook.add_worksheet(
            name=str(item)
        )
        employee_page.set_header('&C' + str(item) + ' Schedule')
        employee_page.hide_gridlines(False)
        employee_page.set_landscape()
        employee_page.fit_to_pages(1, 0)

        employee_page.set_column(0, 7, 20, cell_format_default)

        for key, value in header_names.items():
            employee_page.write(key, value[0], value[1])

        employee_page.write_string(1, 0, str(item), cell_format_name)

        # Schedule - Sunday
        employee_page.write_string(
            row=1,
            col=1,
            string=dow['sunday'],
            cell_format=cell_format_default
        )

        # Schedule - Monday
        employee_page.write_string(
            row=1,
            col=2,
            string=dow['monday'],
            cell_format=cell_format_default
        )

        # Schedule - Tuesday
        employee_page.write_string(
            row=1,
            col=3,
            string=dow['tuesday'],
            cell_format=cell_format_default
        )

        # Schedule - Wednesday
        employee_page.write_string(
            row=1,
            col=4,
            string=dow['wednesday'],
            cell_format=cell_format_default
        )

        # Schedule - Thursday
        employee_page.write_string(
            row=1,
            col=5,
            string=dow['thursday'],
            cell_format=cell_format_default
        )

        # Schedule - Friday
        employee_page.write_string(
            row=1,
            col=6,
            string=dow['friday'],
            cell_format=cell_format_default
        )

        # Schedule - Saturday
        employee_page.write_string(
            row=1,
            col=7,
            string=dow['saturday'],
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
