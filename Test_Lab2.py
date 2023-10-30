import Lab2

def test_find_min_max():
    num_list=[23,30,47,60,67]
    result=[]

    result=Lab2.calc_min_max_temperature(num_list)
    assert (result==(23,67))


def test_calc_average():
    num_list = [23, 30, 47, 60, 67]
    result=[]

    result=Lab2.calc_average_temperature(num_list)
    assert (result==45.4)


def test_median_temperature():
    num_list = [23, 30, 47, 60, 67]
    result=[]

    result=Lab2.calc_median_temp(num_list)
    assert result==47