#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python calendar
Highlights today's date by subclassing HTMLCalendar and modifying formatmonth
and formatday methods.
"""

import calendar
import datetime


class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday=calendar.SUNDAY):
        """
        currentmonth is the month currently being rendered by calendar - used
        in formatday() to identify the current month/day combination to apply
        the custom css style.
        """
        super(CustomHTMLCalendar, self).__init__(firstweekday)
        self.currentmonth = None

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        # Modified to apply a custom css style for the current month and day.
        today = datetime.datetime.today()
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        elif self.currentmonth == today.month and day == today.day:
            return '<td class="%s">%d</td>' % ('currentday', day)
        else:
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        # Modified to save themonth for use by formatday()
        self.currentmonth = themonth

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)


if __name__ == '__main__':
    """
    formatyearpage() returns bytes, need to decode to turn bytes into string.
    The Ubuntu system default encoding is utf-8, but I specify it here so we
    can also run on Windows.
    """
    year = datetime.datetime.today().year
    cols = 3
    cal = CustomHTMLCalendar(calendar.SUNDAY).formatyearpage(year, cols, 'calendar.css', 'utf-8').decode('utf-8')
    print(cal)
