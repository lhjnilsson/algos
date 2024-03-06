from multiprocessing import set_start_method

from first import random 

from foreverbull import entity

set_start_method("spawn")


def test_positive_returns(foreverbull):
    with foreverbull(random, []) as fb:
        fb.configure_execution(entity.backtest.Execution())
        fb.run_execution()
