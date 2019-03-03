from datetime import timedelta, date


class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """
    매번 새로운 DateRangeContainerIterable 인스턴스를 만듦
    한번에 하나의 날짜만 생성하여 메모리 적게 잡아 먹음 but 인덱싱 x
    """
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        cnt_day = self.start_date
        while cnt_day < self.end_date:
            yield cnt_day
            cnt_day += timedelta(days=1)


class DateRangeSequence:
    """인덱싱을 하기 위해 리스트로 저장"""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        cnt_day = self.start_date
        while cnt_day < self.end_date:
            days.append(cnt_day)
            cnt_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]



if __name__ == '__main__':
    # test DateRangeIterable
    for day in DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5)):
        print(day)

    # test DateRangeContatinerIterable
    r1 = DateRangeContainerIterable(date(2019, 1, 1), date(2019, 1, 5))
    print(",".join(map(str, r1)))
    print('max of r1: {}'.format(max(r1)))

    # test DateRangeSequence
    s1 = DateRangeSequence(date(2019, 1, 1), date(2019, 1, 5))
    for day in s1:
        print(day)

    print('first day: {}'.format(s1[0]))
    print('lasy day: {}'.format(s1[-1]))